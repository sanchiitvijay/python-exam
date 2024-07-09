class SavingsAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def check_balance(self):
        print(f"Current balance for account {self.account_number}: ${self.balance}")

account1 = SavingsAccount(1001, "John Doe", 1000)

account1.deposit(500)
account1.withdraw(200)

account1.check_balance()

# Uncomment to test invalid deposit and insufficient balance
# account1.deposit(-100)
# account1.withdraw(3000)
