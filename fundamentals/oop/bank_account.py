class BankAccount:

    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount: 
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

checking = BankAccount(0.1, 100)
savings = BankAccount(0.2, 500)

# checking.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

# savings.deposit(1000).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

# BankAccount.all_accounts()

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.4, 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self

melissa = User("Melissa Cheng", "melcheng12@gmail.com")
melissa.make_deposit(50)
melissa.display_user_balance()