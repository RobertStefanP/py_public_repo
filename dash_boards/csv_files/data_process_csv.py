import pandas as pd


class Calculate():
    def __init__(self):
        self.data = pd.read_csv("superstore.csv")

    def get_sales(self):
        return self.data["Sales"]

    def customer_sales(self):
        pass
    
     
     
if __name__ == "__main__":
    calculate = Calculate()
    print(calculate.data)
    