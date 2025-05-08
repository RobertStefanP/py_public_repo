import sys

from owner import Owner
from account import BankAccount


if __name__ == '__main__':
    owner = Owner('Gigel', 1000)
    owner2 = Owner('Jhon', 2000)
    oner3 = Owner('Cristina', 1500)

    bank = BankAccount(owner.owner, owner.total_money)

    while True:
        print(f"""Choose an option:
            1. Check account
            2. Create bank account
            3. Make a deposit
            4. Make whithdraw
            5. Check balances
            6. Check interest fees
            7. Check all accounts
            8. Exit""")
        opcion = input('Choose an option: ')

        if opcion == '1':
            searched_id = input("Enter the id to search: ")
            account = bank.check_account(searched_id)
            if bank.accounts:
                if account is None:
                    print(F"No accounts have the id {searched_id}, try again.")
                else:
                    print(f"""\nAccount founded: 
                    id: {account.get('id')}
                    owner: {account.get('owner')}
                    balance: {account.get('balance')}""")
            else:
                print("No accounts available. Add some.")

        elif opcion == '2':
            owner = input("Insert the name of the owner: ")
            balance = float(input("Insert the ammount: "))
            new_account = bank.create_bank_account(owner, balance)
            print(new_account)
            print(f"Your account with id: {bank.unique_id} was created {owner}, your balance is {balance}.")

        elif opcion == '3':           
            account = bank.make_deposit()
            if account is None:
                print(f"Account does not exist.")
            else:
                print(f"New balance for {account.get('owner')}: {account.get('balance')}")
                
        elif opcion == '4':
            bank.make_whithdraw()

        elif opcion == '5':
            pass

        elif opcion == '6':
            pass

        elif opcion == '7':
            bank.check_all_accounts()

        elif opcion == '8':
            sys.exit()
            
        else:
            print(f"{opcion} is not a valid opcion, try again.")
