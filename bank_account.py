
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        self.account_balance -= amount
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self 

    def display_account_info(self):
        # your code here
    def yield_interest(self):
        # your code here