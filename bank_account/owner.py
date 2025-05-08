class Owner:
    def __init__(self, owner, total_money):
        self.owner = owner
        self.total_money = total_money

    def __str__(self):
        f"Owner: {self.owner}, Available: {self.total_money}"

    def show_info(self):
        print(f"Owner of the account: {self.owner}, Available funds: {self.total_money}")