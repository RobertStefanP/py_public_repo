from prints import print_order_status
from prints import print_error


class EventHandler:
    def __init__(self, ib, session_manager):
        self.ib = ib 
        self.session_manager = session_manager
        self.is_connected = False
        self.ib.orderStatusEvent += self.on_order_update
        self.ib.newOrderEvent += self.on_order_update
        self.ib.cancelOrderEvent += self.on_order_update
        self.ib.openOrderEvent += self.on_order_update
        
    def on_order_update(self, trade):
        if not self.is_connected:
            return        
        try:                                   
            print_order_status(trade)   
        except Exception as e:
            print_error(str(e))
    