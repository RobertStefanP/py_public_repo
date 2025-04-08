import time
from ib_insync import MarketOrder, LimitOrder

from log_to_file import log_to_file
from prints import print_error


class TradeExecution:
    def __init__(self, ib, contract, session_manager, timing_manager):
        self.ib = ib  
        self.contract = contract  
        self.session_manager = session_manager  
        self.timing_manager = timing_manager  
        
    def place_bracket_order(self, current_price, signal_type):
        try: 
            if not current_price:
                return None, None
        
            sl = current_price - 6 if signal_type == 'bullish' else current_price + 6
            tp = current_price + 10 if signal_type == 'bullish' else current_price - 10
        
            parent_order = MarketOrder('BUY' if signal_type == 'bullish' else 'SELL', 2)
            parent_order.transmit = False 
                    
            self.ib.placeOrder(self.contract, parent_order) 
            time.sleep(1) 
            
            if parent_order.orderId == 0:
                return None, None
                    
            stop_loss_order = self.timing_manager.stoploss_type(signal_type, sl)
            stop_loss_order.parentId = parent_order.orderId
            stop_loss_order.transmit = False
                    
            take_profit_order = LimitOrder('SELL' if signal_type == 'bullish' else 'BUY', 2, tp)
            take_profit_order.parentId = parent_order.orderId 
            take_profit_order.transmit = True    
            take_profit_order.outsideRth = True 
            
            self.ib.placeOrder(self.contract, stop_loss_order)
            self.ib.placeOrder(self.contract, take_profit_order)
            
            self.session_manager.monitoring_orders_mode = True

            return sl, tp
        
        except Exception as e: 
            print_error(str(e))
            
            return None, None
