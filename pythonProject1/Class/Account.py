class Account:
    def __init__(self, account_number, balance = 0):
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        self.balance -= amount

    def deposit (self, amount):
            self.balance += amount

gastt_acct = Account("011817490")
gastt_acct.deposit(1500)
gastt_acct.withdraw(250)

print(gastt_acct.balance)


