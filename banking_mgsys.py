# BANKING SYSTEM WITH SQL

import sqlite3

# Connect to DB
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    username TEXT PRIMARY KEY,
    pin TEXT,
    balance REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    type TEXT,
    amount REAL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()


class BankingSystem:

    def create_account(self):
        print("\n========= CREATE NEW ACCOUNT =========")
        username = input("Enter a username: ").lower()

        cursor.execute("SELECT * FROM accounts WHERE username=?", (username,))
        if cursor.fetchone():
            print("Username already exists!")
            return

        pin = input("Set a 4-digit PIN: ")
        if not (pin.isdigit() and len(pin) == 4):
            print("PIN must be exactly 4 digits.")
            return

        try:
            balance = float(input("Enter initial deposit amount: ₹"))

            cursor.execute("INSERT INTO accounts VALUES (?, ?, ?)",
                           (username, pin, balance))
            conn.commit()

            print(f"Account created successfully for '{username}'!")
        except ValueError:
            print("Invalid input!")

    def login(self):
        print("\n========= LOGIN =========")
        username = input("Enter your username: ").lower()
        import getpass
        pin = getpass.getpass("Enter PIN: ")

        cursor.execute("SELECT * FROM accounts WHERE username=? AND pin=?",
                       (username, pin))
        account = cursor.fetchone()

        if account:
            print(f"\nWelcome, {username}!")
            self.start_menu(username)
        else:
            print("Invalid username or PIN!")

    def check_balance(self, username):
        cursor.execute("SELECT balance FROM accounts WHERE username=?", (username,))
        result = cursor.fetchone()
        if result:
            balance = result[0]
            print(f"Current Balance: ₹{balance}")
        else:
           print("Account not found!")


    def deposit(self, username):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                cursor.execute("UPDATE accounts SET balance = balance + ? WHERE username=?",
                               (amount, username))
                cursor.execute(
                   "INSERT INTO transactions (username, type, amount) VALUES (?, ?, ?)",
                    (username, "DEPOSIT", amount)
                )

                conn.commit()
                print("Deposit successful!")
            else:
                print("Invalid amount!")
        except ValueError:
            print("Invalid input!")

    def withdraw(self, username):
        try:
             amount = float(input("Enter amount to withdraw: ₹"))

             cursor.execute("SELECT balance FROM accounts WHERE username=?", (username,))
             result = cursor.fetchone()

             if not result:
                print("Account not found!")
                return

             balance = result[0]

             if amount > balance:
              print("INSUFFICIENT BALANCE!")
             elif amount <= 0:
               print("Invalid amount!")
             else:
               cursor.execute(
                 "UPDATE accounts SET balance = balance - ? WHERE username=?",
                 (amount, username)
               )

               cursor.execute(
                 "INSERT INTO transactions (username, type, amount) VALUES (?, ?, ?)",
                 (username, "WITHDRAW", amount)
               )

               conn.commit()
               print("Withdrawal successful!")
        except ValueError:
          print("Invalid input!")

    def view_transactions(self, username):
       cursor.execute(
        "SELECT type, amount, date FROM transactions WHERE username=?",
        (username,)
       )
       rows = cursor.fetchall()

       print("\n====== TRANSACTION HISTORY ======")
       print("TYPE       | AMOUNT | DATE")
       print("----------------------------------")

       for row in rows:
          print(f"{row[0]} | ₹{row[1]} | {row[2]}")        

    def start_menu(self, username):
        while True:
            print("\n============ ATM MENU ============")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transactions")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance(username)
            elif choice == "2":
                self.deposit(username)
            elif choice == "3":
                self.withdraw(username)
            elif choice == "4":
                self.view_transactions(username)
            elif choice == "5":
                print("Logging out...")
                break

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
                print("THANK YOU FOR USING OUR ATM!")
                break
            else:
                print("Invalid option!")


# Run program
bank = BankingSystem()
bank.main()