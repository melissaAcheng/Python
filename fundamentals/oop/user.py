class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    # add deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    # add withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # add display balance method
    def display_user_balance(self):
        print(f"User: {self.name}, {self.account_balance}")
        return self

    # add transfer amount method
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self


melissa = User("Melissa Cheng", "melcheng12@gmail.com")
thomas = User("Thomas Chang", "tomchang93@gmail.com")
katie = User("Katie Cheng", "katielynn842@gmail.com")

melissa.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(50).display_user_balance()
thomas.make_deposit(300).make_deposit(200).make_withdrawal(200).display_user_balance()
katie.make_deposit(1000).make_withdrawal(200).make_withdrawal(40).make_withdrawal(50).display_user_balance()

melissa.transfer_money(thomas, 50)