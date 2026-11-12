
from decimal import Decimal, InvalidOperation


class BankAccount:
    def __init__(self, owner, balance=0, backup=0):
        self.__owner = owner
        self.__balance = Decimal(str(balance))
        self.__backup = Decimal(str(backup))

        if not self.__owner.strip():
            raise ValueError("put a valid name my love.")

        if self.__balance < 0 or self.__backup < 0:
            raise ValueError("you cant be that poor!!")

    def deposit(self, amount, account):
        if amount <= 0:
            print("Error: at least borrow from someone youve literally got nothing!!")
            return

        if account == 1:
            self.__balance += amount
            print("Deposit successful yayyy!")

        elif account == 2:
            self.__backup += amount
            print("Backup deposit successful yayyy!")

        else:
            print("Error: Invalid account boooo!!!.")

    def withdraw(self, amount, account):
        if amount <= 0:
            print("Error: dont be this avaricious!! get more than zero.")
            return

        if account == 1:
            if amount > self.__balance:
                print("Error: not enough in the account sorry!!!")
                return

            self.__balance -= amount
            print("Withdrawal successful yayyy!")

        elif account == 2:
            if amount > self.__backup:
                print("Error: not enough in the backup account sorry!!!")
                return

            self.__backup -= amount
            print("Withdrawal successful yaayyyy!")

        else:
            print("Error: Invalid account boooo!!!.")

    def show_balance(self, account):
        if account == 1:
            print("Original Balance:", self.__balance)

        elif account == 2:
            print("Backup Balance:", self.__backup)

        else:
            print("Error: Invalid account.")

    def get_amount(self):
        while True:
            try:
                value = input("Enter amount: ").strip()

                amount = Decimal(value)

                if not amount.is_finite():
                    print("Error: Enter a valid number.")
                    continue

                if amount <= 0:
                    print("Error: Amount must be positive.")
                    continue

            except InvalidOperation:
                print("Error: Please enter numbers only.")

    def get_account(self):
        while True:
            try:
                account = int(
                    input("1. Original Account / 2. Backup Account: ")
                )

                if account in (1, 2):
                    return account

                print("Error: Choose 1 or 2.")

            except ValueError:
                print("Error: Enter 1 or 2.")

    def menu(self):
        while True:
            try:
                print("\n===== PRIVATE BANK SYSTEM =====")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Exit")

                choice = input("Choose an option: ").strip()

                if choice == "1":
                    amount = self.get_amount()
                    account = self.get_account()
                    self.deposit(amount, account)

                elif choice == "2":
                    amount = self.get_amount()
                    account = self.get_account()
                    self.withdraw(amount, account)

                elif choice == "3":
                    account = self.get_account()
                    self.show_balance(account)

                elif choice == "4":
                    print("Thank you for using Private Bank!")
                    break

                else:
                    print("Invalid option! Choose 1-4.")

            except (EOFError, KeyboardInterrupt):
                print("\nBank system closed safely yayyy.")
                break



my_bank = BankAccount("rowan", 1000, 500)


my_bank.menu()
