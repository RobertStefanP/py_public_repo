from prints import print_error


class SignalDetection:
    def __init__(self, data_handler, difference_size=0.50): 
        self.data_handler = data_handler  
        self.difference_size = difference_size 
        self.bars_below = 0  
        self.bars_above = 0 
        self.bars_above_details = [] 
        self.bars_below_details = [] 
                
    