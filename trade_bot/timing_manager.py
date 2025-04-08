from datetime import time, datetime, timedelta
from ib_insync import StopOrder, StopLimitOrder


class TimingManager:
    def __init__(self, ib, contract, session_manager):
        self.ib = ib  
        self.contract = contract  
        self.session_manager = session_manager  
        self.start_time = time(15, 31)
        self.end_time = time(21, 55)
        
    def calculate_next_signal_check_time(self):
        current_time = datetime.now()  
        minutes_to_next_run = 5 - (current_time.minute % 5)  
        seconds_to_next_run = (minutes_to_next_run * 60) - current_time.second + 8  

        if seconds_to_next_run < 8:  
            seconds_to_next_run += 5 * 60  
        return current_time + timedelta(seconds=seconds_to_next_run) 
    
    def stoploss_type(self, signal_type, sl):
        current_time = datetime.now().time() 
        
        if self.start_time <= current_time < self.end_time: 
            return StopOrder('SELL' if signal_type == 'bullish' else 'BUY', 1, sl, outsideRth=True)
        else: 
            stop_price = sl - 0.25 if signal_type == 'bullish' else sl + 0.25 
            return StopLimitOrder('SELL' if signal_type == 'bullish' else 'BUY', 1, stop_price, sl, outsideRth=True)
        