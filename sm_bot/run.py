""" 
Cross over detection.
-Works well, probably should be tested in a different time frame with different 
sma/ema.
"""

import threading
from datetime import datetime
from ib_insync import Future

from broker_connection import BrokerConnection
from session_manager import SessionManager, OrderEvent
from signal_detector import SignalDetector
from timing_manager import TimingManager
from trade_execution import TradeExecution
from telegram_msg import telegr_msg
from prints import print_error


if __name__ == "__main__":     
    broker = BrokerConnection(host='127.0.0.1', port=7497, clientId=1) 
    contract = Future(symbol='MES', lastTradeDateOrContractMonth='20250620', exchange='CME')
    session = SessionManager(broker.ib, contract)    
    signal = SignalDetector(broker.ib, contract) 
    timing = TimingManager(broker.ib, contract) 
    execution = TradeExecution(broker.ib, contract, timing) 
    events = OrderEvent(broker.ib, session) 
    thread = threading.Event()
    
    try:
        time = datetime.now().strftime('%H:%M:%S')
        contract = contract.symbol    
        print(f"{time} - Starting bot. Trading {contract} contract.")        
        while True:
            while broker.trading_hours():        
                if not broker.ib.isConnected(): 
                    time = datetime.now().strftime('%H:%M:%S')
                    telegr_msg(f"{time} - Attempting connection...")                                                               
                    result = broker.connect()
                    if result != "connected" or broker.last_error:
                        telegr_msg(f"{time} - {result}")
                    else:
                        print(f"{time} - ...clientId {broker.clientId} connected.")                      

                    while broker.trading_hours():         
                        time = datetime.now().strftime('%H:%M:%S')              
                        session.orders()
                        session.positions()                              
                        print(f"{time} - Startup check done.")
                                               
                        while not session.orders or not session.positions: 
                            time = datetime.now().strftime('%H:%M:%S')                                 
                            print(f"{time} - Orders/positions active at startup. Waiting to be filled/canceled.")                                                         
                            broker.ib.sleep(60)

                            time = datetime.now().strftime('%H:%M:%S')
                            print(f"\n{time} - Checking...")                                                        
                            session.orders()
                            session.positions()
                            if not session.orders and not session.positions: 
                                session.monitoring = False                                                                                                
                                continue                   
                        else:
                            print(f"{time} - ...no open orders/positions found.") 
                                                       
                        while True:
                            time = datetime.now().strftime('%H:%M:%S')
                            print(f"{time} - Waiting until the next signal check.")                            
                            next_run = timing.next_signal()
                            wait_sec = (next_run - datetime.now()).total_seconds()                
                            thread.wait(wait_sec) 
                                                      
                            thread.clear()                           
                            data = signal.fetch_data('2 D', '5 mins', 'TRADES')                                                                                                                                
                            if data is None or data.empty:
                                time = datetime.now().strftime('%H:%M:%S') 
                                print(f"{time} - No historical data available or data is empty.")                                 
                            else:    
                                ind = signal.calculate_indicators(data)                                                                                              
                                if ind is None or ind.empty:
                                    time = datetime.now().strftime('%H:%M:%S')
                                    print(f"{time} - No data to calculate indicators.")   
                                else:
                                    time = datetime.now().strftime('%H:%M:%S')                                                                                                                                                                                                                              
                                    current_price = ind['close'].iloc[-1]
                                    trade, msg = signal.check_signals(ind)
                                    
                                    if trade == 'none':                                        
                                        print(f"\n{time} - BarCls: {ind['close'].iloc[-2]} - EMA: {ind['EMA'].iloc[-2]} and SMA: {ind['SMA'].iloc[-2]}")
                                        print(f"{time} - {msg}")
                                    else:
                                        if trade == 'bullish':
                                            print(f"\n{time} - BarCls: {ind['close'].iloc[-2]} > EMA: {ind['EMA'].iloc[-2]} and SMA: {ind['SMA'].iloc[-2]}")
                                        elif trade == 'bearish':
                                            print(f"\n{time} - BarCls: {ind['close'].iloc[-2]} < EMA: {ind['EMA'].iloc[-2]} and SMA: {ind['SMA'].iloc[-2]}")
                                        print(f"{time} - {msg}")
                                        sl, tp = execution.place_bracket(current_price, trade)                                
                                        print(f"{time} - Price: {current_price} Bracket placed: SL - {sl} TP - {tp}")
                                        telegr_msg(f"{time} - Price: {current_price} Bracket placed: SL - {sl} TP - {tp}")
                                        session.monitoring = True
                                        
                                        while session.monitoring:
                                            time = datetime.now().strftime('%H:%M:%S')
                                            print(f"{time} - Active orders, waiting...")                                                
                                            broker.ib.sleep(60)
                                            
                                            time = datetime.now().strftime('%H:%M:%S')
                                            print(f"\n{time} - Checking...")                                              
                                            session.orders()
                                            session.positions()                                                
                                            if not session.orders and not session.positions: 
                                                session.monitoring = False                                                                                                                                                                                                
                                                break                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            time = datetime.now().strftime('%H:%M:%S')
            time_left = broker.time_left()
            print(f"{time} - Outside trading hours, time left: {time_left}")            
            broker.ib.sleep(300)     
                       
    except Exception as e:
        time = datetime.now().strftime('%H:%M:%S')         
        telegr_msg(f"{time} - Critical error in main loop: {e}")    
    except KeyboardInterrupt:
        time = datetime.now().strftime('%H:%M:%S')
        print(f"{time} - Closing MESbot!")           
    finally:        
        time = datetime.now().strftime('%H:%M:%S')
        result = broker.disconnect() 
        telegr_msg(f"{time} - {result.title()} from IB.")
            