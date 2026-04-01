#ATM_TASK
'''User authentication (PIN check)
Check balance
Deposit money
Withdraw money
Exit safely'''


class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin
    def check_pin(self):
        enter_pin = int(input("enter the pin number:"))
        if enter_pin == self.pin:
            return True
        else:
            print("invalid pin code!")
            return False
        
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")
    
    def deposit(self):
        amount = float(input("Enter the amount for deposit: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} has been deposited...")
            self.check_balance
        else:
            print("Transaction failed!")

    def withdraw(self):
        amount = float(input("Enter the amount for withdraw: ₹"))
        if amount > self.balance:
            print(f"Insufficient Balance!")
        elif amount < 0:
            print(f"Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} has been withdrawn successfully...")

    def start(self):
        print("============WELCOME TO ATM============")
        if not self.check_pin():
            return
        
        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("THANK YOU VISIT AGAIN...")
                break
            else:
                print("Invalid option!")

atm =ATM(balance = 5000, pin = 1234)
atm.start()

                
