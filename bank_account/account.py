from random import randint
from owner import Owner
import re


class BankAccount():
    interest = 3.5
    total_accounts = 0
    unique_id = 0

    def __init__(self):
        self.accounts = []

    def __str__(self):
        return f"Total accounts: {BankAccount.total_accounts}, Interests: {BankAccount.interest}"
    
    def check_account(self):
        found = False
        search_id = input("Enter the searched id: ")
        if search_id.isdigit():
            searched_id = int(search_id)
            if self.accounts: 
                if searched_id:            
                    for account in self.accounts:
                        if account.get('id') == searched_id:
                            found = True
                            print(f"""Account id {searched_id} was found: {account.get('owner')}""")
                            break       
                    if not found:
                        print(f"Account with Id {searched_id} was not found.")
            else:
                print(f"\nNo accounts registered, add some clients.")
        else:
            print(f"{search_id} is not valid, try again.")

    def create_bank_account(self):
        name = input("Name of the account owner: ")
        if re.fullmatch(r"[a-zA-Z]{3,15}",name):
            BankAccount.unique_id = randint(1, 9999)
            while any(account['id'] == BankAccount.unique_id for account in self.accounts):
                BankAccount.unique_id = randint(1, 9999)
        
            money_account = input("The ammount of the account: ")
            if money_account.isdigit():
                money = int(money_account)
                owner = Owner(name, money)
                account = {
                        'id': BankAccount.unique_id,
                        'owner': owner,
                        }
                self.accounts.append(account)             
                BankAccount.total_accounts +=1
                print(f"""\nNew account created successfully:
                    Id: {account['id']}
                    Name: {account['owner'].name.title()}
                    Balance: {account['owner'].money}""")                   
            else:
                print(f"{money_account} is not valid, try again.")       
        else:
            print(f"""'{name}' is not a valid name, min 3 characters,  15 max,
                  no numbers!""")

    def make_deposit(self):   
        found = False
        acc_id = input("Enter account id: ")
        if acc_id.isdigit():
            account_id = int(acc_id)
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
        else:
            print(f"{acc_id} is not valid, try again.")            

    def make_whithdraw(self):
        found = False
        if self.accounts:
            acc_id = input("Enter the account id: ")
            if acc_id.isdigit():
                account_id = int(acc_id)
                for account in self.accounts:
                    if account.get('id') == account_id:
                        found = True
                        whithdraw_amount = input("The amount to whithdraw: ") 
                        if whithdraw_amount.isdigit():
                            amount = int(whithdraw_amount)
                            if account['owner'].money >= amount:                           
                                balance = account['owner'].money
                                balance -=amount
                                account['owner'].money = balance
                                print(f"Whithdraw successfully. New balance: {account['owner'].money}")
                                break
                            else:                           
                                print(f"Insufficient funds, available: {account['owner'].money}, try again.")
                                break       
                        else:
                            print(f"{whithdraw_amount} is not valid, try again.")                    
                if not found:
                    print(f"Account Id {account_id} not found, try again.")
            else:
                print(f"{acc_id} is not valid, try again.")
        else:                           
            print("No accounts, add some clients first.")
    
    def check_all_accounts(self):
        if self.accounts:
            for account in self.accounts:            
                print(f"Id: {account.get('id')}, Name: {account['owner'].name}, Balance: {account['owner'].money}")
        else:
            print(f"No accounts availble, add some clients.")

    @classmethod
    def change_interest_fee(cls):
        old_interest = BankAccount.interest 
        insert_fee = input("Enter the new fee: ")
        if insert_fee.isdigit():
            new_fee = int(insert_fee)
            if new_fee > old_interest:
                BankAccount.interest = new_fee
                print(f"We increase our prices, new interest fee: {new_fee} %")
            else:
                print(f"We decrease our prices, new interest fee: {new_fee} %")
        else:
            print(f"{insert_fee} is not valid, try again.")
