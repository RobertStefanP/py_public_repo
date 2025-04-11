from datetime import datetime
from email import message
from ib_insync import Future

from telegram_message import send_telegram_message
from prints import log_to_file
from broker_connection import BrokerConnection
from session_manager import SessionManager
from signal_detector import SignalDetector
from timing_manager import TimingManager
from event_handler import EventHandler
from trade_execution import TradeExecution
from prints import print_error


if __name__ == "__main__":     
    broker = BrokerConnection(host='127.0.0.1', port=7497, clientId=2) 
    contract = Future(symbol='MES', lastTradeDateOrContractMonth='20250620', exchange='CME')
    session_manager = SessionManager(broker.ib, contract)    
    signal_detector = SignalDetector(broker.ib, contract) 
    timing_manager = TimingManager(broker.ib, contract, session_manager)
    event_handler = EventHandler(broker.ib, session_manager)
    trade_execution = TradeExecution(broker.ib, contract, session_manager, timing_manager)

    try:
        timestamp = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')    
        print(f"{timestamp} - Starting bot")
        while True:
            while broker.trading_hours():        
                if not broker.ib.isConnected(): 
                    current_time = datetime.now().strftime('%H:%M:%S')
                    send_telegram_message(f"{current_time} - Attempting connection...")                                           
                    result = broker.connect()
                    if result != "connected" or broker.last_error:
                        send_telegram_message(f"{timestamp} - {result}")
                    else:
                        print(f"{current_time} - ...clientId {broker.clientId} connected.")   
                    event_handler.is_connected = True

                    while broker.trading_hours():          
                        current_time = datetime.now().strftime('%H:%M:%S')              
                        session_manager.check_orders()
                        session_manager.check_positions()                              
                        print(f"{current_time} - Startup check done.")

                        while session_manager.open_orders or session_manager.open_positions: 
                            current_time = datetime.now().strftime('%H:%M:%S')     
                            session_manager.monitoring_orders_mode = True                            
                            print(f"{current_time} - Orders/positions active at startup. Waiting to be filled/canceled.") 
                            broker.ib.sleep(30)

                            current_time = datetime.now().strftime('%H:%M:%S')
                            print(f"\n{current_time} - Checking...")
                            session_manager.check_orders()
                            session_manager.check_positions()

                            if not session_manager.open_orders and not session_manager.open_positions: 
                                monitoring_orders_mode = False                                                                                                
                                continue                   
                        else:
                            print(f"{current_time} - ...no open orders/positions found.") 
                            
                        while True:
                            current_time = datetime.now().strftime('%H:%M:%S')
                            print(f"{current_time} - Waiting untill the next signal check.")

                            next_run_time = timing_manager.calculate_next_signal_check_time()
                            wait_seconds = (next_run_time - datetime.now()).total_seconds()                
                            session_manager.update_event.wait(wait_seconds)
                            session_manager.update_event.clear()                           
                            historical_data = signal_detector.fetch_historical_data('2 D', '5 mins', 'TRADES')
                                                                                                                                
                            if historical_data is not None and not historical_data.empty:
                                current_time = datetime.now().strftime('%H:%M:%S') 
                                indicators = signal_detector.calculate_indicators(historical_data)                                  
                                                            
                                if indicators is not None and not indicators.empty:                                                                                                                                                                                                                                
                                    current_time = datetime.now().strftime('%H:%M:%S')
                                    current_price = indicators['close'].iloc[-1]                                                                                                                                                                   
                                    indicators_value = signal_detector.check_crossover(indicators)  
                                                                                
                                    if indicators_value:  
                                        current_time = datetime.now().strftime('%H:%M:%S')                                     
                                        signal, message = signal_detector.check_signals()
                                        position = indicators_value 
                                        print(f"{current_time} - Long: bear, bull, bull")
                                        print(f"{current_time} - Short: bull, bear, bear")
                                        print(f"{current_time} - Current: {position[-3]}, {position[-2]}, {position[-1]}")
                                        print(f"{current_time} - {message}")      
                                                                               
                                        if signal is not None:                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                            sl, tp = trade_execution.place_bracket_order(current_price, signal)                                            
                                            print(f"{current_time} - Bracket order placed, with SL at {sl} and TP at {tp}")                                                
                                            session_manager.monitoring_orders_mode = True
                                            
                                            while session_manager.monitoring_orders_mode:
                                                current_time = datetime.now().strftime('%H:%M:%S')
                                                monitoring_orders_mode = True
                                                print(f"{current_time} - Active orders, waiting...")
                                                broker.ib.sleep(30)

                                                current_time = datetime.now().strftime('%H:%M:%S')
                                                print(f"\n{current_time} - Checking...")

                                                session_manager.check_orders()
                                                session_manager.check_positions()                                                
                                                if not session_manager.open_orders and not session_manager.open_positions: 
                                                    monitoring_orders_mode = False                                                                                                
                                                    break                                       
                                    else:
                                        pass             
                                else:
                                    print(f"{current_time} - No data to calculate indicators.")                                                                                                                                                    
                            else:
                                print(f"{current_time} - No historical data available or data is empty.")                                
            current_time = datetime.now().strftime('%H:%M:%S')
            time_left = broker.time_left()
            print(f"{current_time} - Outside trading hours, time left: {time_left}")
            broker.ib.sleep(300)
                
    except Exception as e:
        current_time = datetime.now().strftime('%H:%M:%S')         
        send_telegram_message(f"{current_time} - Critical error in main loop: {e}")    
    except KeyboardInterrupt:
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f"{current_time} - Manually closing MESbot!")           
    finally:        
        current_time = datetime.now().strftime('%H:%M:%S')
        result = broker.disconnect() 
        send_telegram_message(f"{current_time} - {result.title()} from IB.")
            