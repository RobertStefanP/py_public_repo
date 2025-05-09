from datetime import datetime
from ib_insync import util
import pandas as pd
from prints import print_error


class SignalDetector:
    def __init__(self, ib, contract):        
        self.ib = ib  
        self.contract = contract  
        self.first_run = True  
        self.indicators_value = []  
        
    def fetch_historical_data(self, duration, bar_size, what_to_show):         
        bars = self.ib.reqHistoricalData(
            self.contract,  
            endDateTime='',  
            durationStr=duration,  
            barSizeSetting=bar_size,  
            whatToShow=what_to_show,  
            useRTH=False,  
            formatDate=1)          
        df = util.df(bars) if bars else None 
               
        if df is not None:
            df = df[['date', 'open', 'high', 'low', 'close']]        
        return df

    def calculate_indicators(self, data): 
        if data is not None and not data.empty:              
            data['midpoint'] = (data['high'] + data['low']) / 2  
            data['EMA'] = data['midpoint'].ewm(span=10, adjust=False).mean().round(2) 
            data['SMA'] = data['midpoint'].rolling(window=20).mean().round(2)  
            
            data['EMA'] = data['EMA'].round(2) 
            data['SMA'] = data['SMA'].round(2) 
                        
            data = data.tail(20)                                   
            return data 
        else:
            return None

    def check_crossover(self, indicators): 
        try:
            values_list = []            
            if indicators is None or indicators.empty:
                return "No data to calculate crossover"    
            
            for index, row in indicators.iterrows():
                ema, sma = row['EMA'], row['SMA']                            
                if ema > sma:
                    values_list.append('bull')  
                elif ema < sma:
                    values_list.append('bear')
                elif ema == sma:
                    values_list.append('equal')                                                        
            self.indicators_value = values_list[-10:]
             
            return self.indicators_value                                                                               
        except Exception as e:            
            print_error(str(e)) 
            return str(e)       
    
    def check_signals(self):
        try:
            if self.indicators_value:                                                               
                if (self.indicators_value[-3] != self.indicators_value[-2] and 
                    self.indicators_value[-2] == self.indicators_value[-1]):                               
                    if self.indicators_value[-1] == 'bull':
                        return 'bullish', 'BULLISH signal detected!'            
                    if self.indicators_value[-1] == 'bear':
                        return 'bearish', 'BEARISH signal detected!'                                      
            return None, 'NO signal detected!'            
        except Exception as e:            
            print_error(str(e)) 
            return 'error', str(e)      
              