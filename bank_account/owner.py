class Owner:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return f"Owner: {self.name}, Available: {self.money}"

    def show_info(self):
        print(f"Owner of the account: {self.name}, Available funds: {self.money}")