class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Stan konta: {self.balance}")

konto = BankAccount(100)
konto.deposit(50)
konto.withdraw(100)
konto.show_balance()