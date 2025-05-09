import sys

from owner import Owner
from account import BankAccount


if __name__ == '__main__':
    owner = Owner('Gigel', 1000)
    owner2 = Owner('Jhon', 2000)
    owner3 = Owner('Cristina', 1500)

    bank = BankAccount(owner.owner, owner.total_money)

    while True:
        print(f"""\nChoose an option:
            1. Check account
            2. Create bank account
            3. Make a deposit
            4. Make whithdraw
            5. Change interest fees
            6. Check all accounts
            7. Check total accounts.
            8. Exit""")
        opcion = input('Choose an option: ')

        if opcion == '1':
            bank.check_account()

        elif opcion == '2':
            unique_id, owner, balance = bank.create_bank_account()
            print(f"""\nNew account created successfully:
                Id: {unique_id}
                Name: {owner}
                Balance: {balance}""")

        elif opcion == '3':           
            account = bank.make_deposit()
            if account is None:
                print(f"\nAccount does not exist, try again.")
            else:
                print(f"""\nDeposit succesfully for account id {account.get('id')}
                    New balance for {account.get('owner')}: {account.get('balance')}""")
                
        elif opcion == '4':
            bank.make_whithdraw()

        elif opcion == '5':
            BankAccount.change_interest_fee()

        elif opcion == '6':
            bank.check_all_accounts()

        elif opcion == '7':
            print(f"\nTotal accounts in our bank: {BankAccount.total_accounts}")
            print(f"Our interest rates: {BankAccount.interest} %")

        elif opcion == '8':
            print("Exiting program.")
            sys.exit()

        else:
            print(f"{opcion} is not a valid opcion, try again.")
