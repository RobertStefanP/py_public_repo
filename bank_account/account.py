from random import randint
from owner import Owner


class BankAccount(Owner):
    interest = 3.5
    total_accounts = 0
    unique_id = 0
    def __init__(self, name, money):
        super().__init__(name, money)
        self.accounts = []
        BankAccount.total_accounts += 1

    def __str__(self):
        return f"Total accounts: {BankAccount.total_accounts}, Interests: {BankAccount.interest}"
    
    def check_account(self):
        found = False
        searched_id = int(input("Enter the searched id: "))
        if self.accounts: 
            if searched_id:            
                for account in self.accounts:
                    if account.get('id') == searched_id:
                        found = True
                        print(f"""Account with id {searched_id} founded:
                        Owner: {account.get('owner')}
                        Balance: {account.get('balance')}""")
                        break       
                if not found:
                    print(f"Account with Id {searched_id} not found.")
        else:
            print(f"\nNo accounts registered, add some clients.")
        
    def create_bank_account(self):
        name = input("Insert the owner of the account: ")
        if name:
            BankAccount.unique_id = randint(1000, 9999)
            for account in self.accounts:
                if account.get('id') == BankAccount.unique_id:
                    print(f"Id {BankAccount.unique_id} alredy in use, try a new one.")
            money = int(input("Insert the ammount of the account: "))
            if money:
                owner = Owner(name, money)
                account = {
                        'id': BankAccount.unique_id,
                        'owner': owner,
                        }
                self.accounts.append(account)             
                BankAccount.total_accounts +=1
                print(f"account: {account}")
                print(owner)
            else:
                print(f"Enter a valid number.")       
        else:
            print(f"{owner} is not a valid name, try again.")
        return account

    def make_deposit(self):   
        found = False
        account_id = int(input("Enter account id: "))
        for account in self.accounts:
            if account.get('id') == account_id:
                found = True
                insert_amount = input("Enter the amount to deposit: ")         
                if insert_amount.isdigit():
                    amount = int(insert_amount)
                    account['owner'].money += amount 
                    print(f"""\nDeposit succesfully for account id {account.get('id')}
                    New balance for {account['owner'].name.title()}: {account['owner'].money}""")
                    break 
                else:
                    print(f"{insert_amount} is not a valid value, try again.")
                    break 
        if not found:
            print(f"Account with id {account_id} not found, try again.")

        
        
                




    def make_whithdraw(self):
        found = False
        account_id = int(input("Enter the account id: "))
        if self.accounts:
            for account in self.accounts:
                if account.get('id') == account_id:
                    found = True
                    amount = int(input("The amount to whithdraw: "))    
                    if account.get('balance') >= amount:                           
                        balance = account.get('balance')
                        balance -=amount
                        account['balance'] = balance
                        print(f"Whithdraw successfully. New balance: {account['balance']}")
                        break
                    else:                           
                        print(f"Insufficient funds, available: {account.get('balance')}")
                        break
            if not found:
                print(f"Account: {account_id} not found, try again.")
        else:                           
            print("No accounts, add some clients first.")
    
    def check_all_accounts(self):
        if self.accounts:
            for account in self.accounts:            
                print(f"Id: {account.get('id')}, Name: {account['owner'].name}, Balance: {account['owner'].money}")
        else:
            print(f"No accounts availble, add some clients.")

    @classmethod
    def change_interest_fee(self):
        old_interest = BankAccount.interest 
        insert_fee = input("Enter the new fee: ")
        if insert_fee.isdigit():
            new_fee = int(insert_fee)
            if new_fee > old_interest:
                BankAccount.interest = new_fee
                print(f"We increase our prices, new interest fee: {new_fee} %")
            else:
                print(f"We decrease our prices, new interest fee: {new_fee}")
        else:
            print(f"{insert_fee} is not valid, try again.")
