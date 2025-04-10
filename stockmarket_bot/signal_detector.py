from datetime import datetime
from ib_insync import util
import pandas as pd
from prints import print_error


class SignalDetector:
    def __init__(self, ib, contract):        
        self.ib = ib  
        self.contract = contract  
        self.first_run = True  
        self.daily_bars_details = []  

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

    def calculate_indicators(self, historical_data): 
        if historical_data is not None and not historical_data.empty:              
            historical_data['midpoint'] = (historical_data['high'] + historical_data['low']) / 2  
            historical_data['EMA'] = historical_data['midpoint'].ewm(span=10, adjust=False).mean().round(2) 
            historical_data['SMA'] = historical_data['midpoint'].rolling(window=20).mean().round(2)  
            
            historical_data['EMA'] = historical_data['EMA'].round(2) 
            historical_data['SMA'] = historical_data['SMA'].round(2) 
                                               
            return historical_data 
        else:
            return None

    def bars_close(self, indicators): 
        try:
            if indicators is None or indicators.empty:
                return None, "No data to calculate indicators"  
                                                                                                      
            if indicators['open'].iloc[-2] < indicators['close'].iloc[-2]:                    
                print(f"Bullish: open:{indicators['open'].iloc[-2]} < close:{indicators['close'].iloc[-2]}")
                return 'bullish', 'BULLISH signal detected!' 
                                
            if indicators['close'].iloc[-2] > indicators['open'].iloc[-2]:                   
                print(f"Bearish: open:{indicators['open'].iloc[-2]} > close:{indicators['close'].iloc[-2]}")
                return 'bearish', 'BEARISH signal detected!'                             
            else:    
                return None, "NO signal detected!"
                                                   
        except Exception as e:            
            print_error(str(e)) 
            return None, str(e)       
                
    
