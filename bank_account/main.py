import sys

from owner import Owner
from account import BankAccount


if __name__ == '__main__':
    bank = BankAccount()

    while True:
        print(f"""\nChoose an option:
            1. Check account
            2. Create bank account
            3. Make a deposit
            4. Make whithdraw
            5. Change interest fees
            6. Check all accounts
            7. Check number of total accounts.
            8. Exit""")
        opcion = input('Choose an option: ')

        if opcion == '1':
            print("\n\tChecking an account.")
            bank.check_account()

        elif opcion == '2':
            print("\n\tCreating a bank account.")
            account = bank.create_bank_account()

        elif opcion == '3':   
            print("\n\tMaking a deposit.")        
            bank.make_deposit()
                
        elif opcion == '4':
            print("\n\tMaking a whithdraw.")
            bank.make_whithdraw()

        elif opcion == '5':
            print("Changing interest fees.")
            BankAccount.change_interest_fee()

        elif opcion == '6':
            print("Checking all the accounts.")
            bank.check_all_accounts()

        elif opcion == '7':
            print(f"\nTotal accounts in our bank: {BankAccount.total_accounts}")
            print(f"Our interest rates: {BankAccount.interest} %")

        elif opcion == '8':
            print("Exiting program.")
            sys.exit()

        else:
            print(f"{opcion} is not a valid opcion, try again.")
