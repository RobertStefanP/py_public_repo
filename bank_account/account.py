from random import randint
from owner import Owner


class BankAccount(Owner):
    interest = 3.5
    total_accounts = 0
    unique_id = 0

    def __init__(self, owner, total_money):
        super().__init__(owner, total_money)
        self.accounts = []
        BankAccount.total_accounts += 1

    def __str__(self):
        return f"Total accounts: {BankAccount.total_accounts}, Interests: {BankAccount.interest}"
    
    def check_account(self, searched_id):
        if self.accounts and searched_id:            
            for account in self.accounts:
                if account.get('id') == searched_id:
                    break
                else:
                    return None
            return account
        else:
            return None
        
    def create_bank_account(self, owner, balance):
        BankAccount.unique_id = randint(1000, 9999)
        BankAccount.total_accounts += 1
        self.accounts.append(
            {
                'id': BankAccount.unique_id,
                'owner': owner,
                'balance': balance
            }
        )
        for new_account in self.accounts:
            if new_account.get('id') == BankAccount.unique_id:
                break
        return new_account

    def make_deposit(self):   
        account_id = int(input("Enter account id: "))    
        for account in self.accounts:
            if account.get('id') == account_id: 
                amount = float(input("Enter the amount to deposit: "))           
                account['balance'] += amount 
                return account  
            break    

    def make_whithdraw(self):
        account = int(input("Enter the account id: "))
        if account:
            amount = int(input("The amount to whithdraw: "))           
            for acc in self.accounts:
                if acc.get('balance') > amount:
                    balance = acc.get('balance')
                    balance -=amount
                    acc['balance'] = balance
                    print(f"Whithdraw successfully. New balance: {acc['balance']}")
                    break
                else:
                    print(f"Insufficient funds, available: {acc.get('balance')}")
                    break
            return account

        print(f"You whithdraw {amount} from your current account.")
    
    def check_balance(self):
        if self.accounts:
            for account in self.accounts:
                print(f"Account Id: {account.get('id')}, Balance: {account.get('balance')}")
        else:
            print("No accounts for the moment, try again later.")

    def check_all_accounts(self):
        if self.accounts:
            for account in self.accounts:
                print(f"Id: {account.get('id')}, Owner: {account.get('owner')}, Balance: {account.get('balance')}")
        else:
            print(f"No accounts availble, add some clients.")

    @classmethod
    def change_interest_fee(self, new_interest):
        new_fee = int(input("Enter the new fee: "))
        if new_fee.isnumeric():
            BankAccount.interest = new_interest
            print(f"New interest fee: {new_interest}")
        else:
            print(f"{new_fee} is not a valid value, try again.")
