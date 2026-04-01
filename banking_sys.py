# BANKING_SYSTEM

class Account:
    def __init__(self, username, pin, balance=0):
        self.username = username
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount} has been deposited successfully!")
                self.check_balance()
            else:
                print("Deposit amount must be greater than 0!")
        except ValueError:
            print("Invalid amount entered!")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: ₹"))
            if amount > self.balance:
                print("INSUFFICIENT BALANCE!")
            elif amount <= 0:
                print("Please enter a valid amount!")
            else:
                self.balance -= amount
                print(f"₹{amount} has been withdrawn successfully!")
                self.check_balance()
        except ValueError:
            print("Invalid amount entered!")


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        print("\n========= CREATE NEW ACCOUNT =========")
        username = input("Enter a username: ").lower()

        if username in self.accounts:
            print("Username already exists! Please choose another one.")
            return

        try:
            pin = input("Set a 4-digit PIN: ")
            if not (pin.isdigit() and len(pin) == 4):
                print("PIN must be exactly 4 digits.")
                return

            balance = float(input("Enter initial deposit amount: ₹"))
            self.accounts[username] = Account(username, pin, balance)
            print(f"\nAccount created successfully for '{username.capitalize()}' with balance ₹{balance}!")
        except ValueError:
            print("Invalid input! Please try again.")

    def login(self):
        print("\n========= LOGIN =========")
        username = input("Enter your username: ").lower()
        pin = input("Enter your PIN: ")

        account = self.accounts.get(username)
        if account and account.pin == pin:
            print(f"\nWelcome, {username.capitalize()}!")
            self.start_menu(account)
        else:
            print("Invalid username or PIN! Please try again.")

    def start_menu(self, account):
        while True:
            print("\n============ ATM MENU ============")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Logout")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                account.deposit()
            elif choice == "3":
                account.withdraw()
            elif choice == "4":
                print("Logging out... Returning to main menu.\n")
                break
            else:
                print("Invalid option! Please try again.")

    def main(self):
        print("============ WELCOME TO BANKING SYSTEM ============")
        while True:
            print("\n1. Create New Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("THANK YOU FOR USING OUR ATM! HAVE A NICE DAY!")
                break
            else:
                print("Invalid option! Please select 1, 2, or 3.")
bank = BankingSystem()
bank.main()
