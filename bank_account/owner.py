class Owner:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return f"Name: {self.name.title()}, Balance: {self.money}"
