import os
import pandas as pd
from datetime import datetime, timedelta
from colorama import init, Fore, Style


def log_to_file(message):   
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())  
    week_start_str = start_of_week.strftime('%Y-%m-%d')  
      
    folder_name = 'WeeklyLog'
    if not os.path.exists(folder_name): 
        os.makedirs(folder_name)
    
    log_file_path = os.path.join(folder_name, f'Log_{week_start_str}.txt')
    
    timestamp = today.strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file_path, 'a') as f:
        f.write(f"{timestamp} - {message}\n")


def print_orders(relevant_orders, brackets):
    current_time = datetime.now().strftime('%H:%M:%S')
    
    if relevant_orders and brackets:  
        for brackets, prices in brackets.items():
            current_time = datetime.now().strftime('%H:%M:%S')
            
            if prices["SellLimit"] and prices["SellStop"]:
                print(f"{current_time} - Bracket order active: SellLimit {prices['SellLimit']} - SellStop {prices['SellStop']}")
            
            if prices["BuyLimit"] and prices["BuyStop"]:
                print(f"{current_time} - Bracket order active: BuyLimit {prices['BuyLimit']} - BuyStop {prices['BuyStop']}")

            if prices["SellLimit"] and prices["StopLimitOrder"]:
                print(f"{current_time} - Bracket order active: SellLimit {prices['SellLimit']} - SellStopLimit {prices['StopLimitOrder']}")

            if prices["BuyLimit"] and prices["StopLimitOrder"]:
                print(f"{current_time} - Bracket order active: BuyLimit {prices['BuyLimit']} - BuyStopLimit {prices['StopLimitOrder']}")
    else:
        print(f"{current_time} - No open orders.")


def print_positions(position_details):
    current_time = datetime.now().strftime('%H:%M:%S')
    if position_details: 
        for pos in position_details:             
            print(f"{current_time} - Position active: {pos['symbol']}, Qty: {pos['position']}, Avg Cost: {pos['avg_cost']}")
    else:
        print(f"{current_time} - No open positions.")


init(autoreset=True)
order_id = {}

def print_order_status(trade):#, order, status, contract, filled, remaining)
    current_time = datetime.now().strftime('%H:%M:%S')
    
    order = trade.order
    status = trade.orderStatus
    contract = trade.contract
    filled = status.filled
    remaining = status.remaining
    
    if status.status not in ['Filled', 'Cancelled']:
        return    
    if order.orderId in order_id:
        return    
    order_id[order.orderId] = status.status
       
    color = Fore.WHITE 
    style = Style.NORMAL
    if status.status == 'Filled':
        if order.orderType == 'STP':
            color = Fore.RED
            style = Style.BRIGHT
        elif order.orderType == 'LMT':
            color = Fore.GREEN
            style = Style.BRIGHT
        elif order.orderType == 'STP LMT':  
            color = Fore.RED
            style = Style.BRIGHT

        elif order.orderType == 'MKT':
            if order.action == 'BUY':
                color = Fore.GREEN
                style = Style.NORMAL
            elif order.action == 'SELL':
                color = Fore.RED
                style = Style.NORMAL
                
    elif status.status == 'Cancelled':
        if order.orderType == 'LMT':
            color = Fore.GREEN
            style = Style.NORMAL
        elif order.orderType == 'STP':
            color = Fore.RED
            style = Style.NORMAL
        elif order.orderType == 'STP LMT':  
            color = Fore.RED
            style = Style.NORMAL
        
    print(style + color + "-" * 50)
    print(f"{current_time} - {style}{color}Order {order.permId} status updated:",
        f"\n{style}{color}Order {status.status}: {contract.symbol} {contract.secType} {contract.lastTradeDateOrContractMonth}, Action: {order.action}",
        f"\n{style}{color}Order Type: {order.orderType}, Quantity: {order.totalQuantity}, Filled: {filled}, Remaining: {remaining}",
        f"\n{style}{color}LMT Price: {getattr(order, 'lmtPrice', 'N/A')}, STP Price: {getattr(order, 'auxPrice', 'N/A')}")


def print_bar_details(bar_details, label="Bar Details"):
        current_time = datetime.now().strftime('%H:%M:%S')
        if bar_details: 
            df = pd.DataFrame(bar_details)             
            columns_to_drop = ["volume", "average", "barCount"]
            df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
            
            df['date'] = pd.to_datetime(df['date'])  
            df = df.sort_values(by='date', ascending=True)  
 
            print(f"{current_time} - {label}:")
            print(df)             
        else:
            print(f"\n{current_time} - {label}: \n\t\tNo data to display.") 


def adjust_price(symbol, price):
    if symbol == 'MES': 
        return price / 5  
    return price


def print_error(error_msg):
    print(f"Error: {error_msg}")
