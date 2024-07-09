class SavingsAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance for account {self.account_number}: ${self.balance}")

try:
    account1 = SavingsAccount(1001, "John Doe", 1000)

    account1.deposit(500)
    account1.withdraw(200)

    account1.check_balance()

    # account1.deposit(-100)  # Uncomment to test invalid deposit
    # account1.withdraw(3000)  # Uncomment to test insufficient balance

except ValueError as ve:
    print(f"Error: {ve}")
