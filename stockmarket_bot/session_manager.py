import threading

from prints import print_orders, print_positions, print_error, print_order_status 


class SessionManager:
    def __init__(self, ib, contract):
        self.ib = ib 
        self.contract = contract 
        self.open_orders = [] 
        self.open_positions = [] 
        self.monitoring_orders = False 
        self.update_event = threading.Event()  
        self.event_handler = EventHandler(self.ib, self)
                         
    def check_orders(self): 
        try:
            self.open_orders.clear()
            active_orders = self.ib.reqAllOpenOrders()
            relevant_orders = []    
            brackets = {}   

            if active_orders:
                for trade in active_orders:   
                    order = trade.order                                
                    contract = trade.contract
                    order_status = trade.orderStatus 
                    if (contract.symbol == self.contract.symbol and
                        contract.lastTradeDateOrContractMonth == self.contract.lastTradeDateOrContractMonth):                                                                        
                        if order_status and order_status.status in ('Submitted', 'PreSubmitted') and order.parentId != 0:
                            relevant_orders.append(order)                                    
                            if order.parentId not in brackets:  
                                brackets[order.parentId] = {
                                    "SellLimit": None, 
                                    "SellStop": None, 
                                    "BuyLimit": None, 
                                    "BuyStop": None, 
                                    "StopLimitOrder": None,
                                }                                                                   
                            if order.action == "BUY":  
                                if order.orderType == "LMT":
                                    brackets[order.parentId]["BuyLimit"] = order.lmtPrice
                                elif order.orderType == "STP":
                                    brackets[order.parentId]["BuyStop"] = order.auxPrice
                                elif order.orderType == "STP LMT":  
                                    brackets[order.parentId]["StopLimitOrder"] = order.auxPrice
                            
                            elif order.action == "SELL":  
                                if order.orderType == "LMT":
                                    brackets[order.parentId]["SellLimit"] = order.lmtPrice
                                elif order.orderType == "STP":
                                    brackets[order.parentId]["SellStop"] = order.auxPrice
                                elif order.orderType == "STP LMT":  
                                    brackets[order.parentId]["StopLimitOrder"] = order.auxPrice                                                 
                            self.monitoring_orders = True 
                            self.open_orders = relevant_orders                  
                print_orders(relevant_orders, brackets)                                                                                                                                                                          
            else:
                self.monitoring_orders = False
                print_orders(relevant_orders, brackets)                
        except Exception as e:
            print_error(str(e))

    def check_positions(self):
        try:
            self.open_positions.clear()
            positions = self.ib.positions()
            position_details = []        
            if positions:            
                self.open_positions = [
                    pos for pos in positions
                    if pos.contract.symbol == self.contract.symbol and
                    pos.contract.lastTradeDateOrContractMonth == self.contract.lastTradeDateOrContractMonth
                ]
                if self.open_positions:
                    for pos in self.open_positions:
                        avg_cost_adjusted = pos.avgCost / float(pos.contract.multiplier)
                        rounded_avg_cost = round(avg_cost_adjusted * 4) / 4
                        formatted_avg_cost = f"{rounded_avg_cost:.2f}"

                        position_details.append({
                            "symbol": pos.contract.symbol,
                            "position": pos.position,
                            "avg_cost": formatted_avg_cost
                        })  
                    self.monitoring_orders = True 
                print_positions(position_details)                
            else:
                self.monitoring_orders = False
                print_positions(position_details)                   
                                      
        except Exception as e: 
            print_error(str(e))

class EventHandler:
    def __init__(self, ib, session_manager):
        self.ib = ib 
        self.session_manager = session_manager
        self.ib.orderStatusEvent += self.on_order_update
        self.ib.cancelOrderEvent += self.on_order_update
        
    def on_order_update(self, trade):       
        try:                                   
            print_order_status(trade)   
        except Exception as e:
            print_error(str(e))
    