import time 
from ib_insync import IB
from datetime import datetime, time as active_time, timedelta


class BrokerConnection:
    def __init__(self, host, port, clientId):
        self.host = host
        self.port = port
        self.clientId = clientId
        self.ib = IB()  
        self.last_error = None
        self.start = active_time(8, 25)
        self.end = active_time(22, 1)

    def connect(self):
        attempt = 0        
        while True:
            try:
                self.ib.connect(self.host, self.port, clientId=self.clientId)
                return "connected"   
                                  
            except Exception as e:
                attempt += 1                                
                self.last_error = f"failed after {attempt} attempts: {e}"                                          
                time.sleep(10) 
            
    def disconnect(self):
        if self.ib.isConnected():
            self.ib.disconnect()
        return "disconnected"

    def trading_hours(self):
        now = datetime.now().time()               
        if self.start  <= now <= self.end:
            return True
        return False

    def time_left(self):
        now = datetime.now().time() 
        now_t = timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        start_t = timedelta(hours=self.start.hour, minutes=self.start.minute, seconds=self.start.second)
        end_t = timedelta(hours=self.end.hour, minutes=self.end.minute, seconds=self.end.second)

        if now_t < start_t:
            time_left = start_t - now_t 
        elif now_t > end_t:
            time_left = timedelta(days=1) - (now_t - start_t)          
        return time_left
   