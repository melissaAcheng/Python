class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    # add deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
    
    # add withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


melissa = User("Melissa Cheng", "melcheng12@gmail.com")
thomas = User("Thomas Chang", "tomchang93@gmail.com")
katie = User("Katie Cheng", "katielynn842@gmail.com")

melissa.make_deposit(200)
melissa.make_deposit(200)
melissa.make_deposit(200)
melissa.make_withdrawal(50)
thomas.make_deposit(300)
thomas.make_deposit(200)
thomas.make_withdrawal(200)
katie.make_deposit(1000)
katie.make_withdrawal(200)
katie.make_withdrawal(40)
katie.make_withdrawal(50)

melissa.display_user_balance()
thomas.display_user_balance()
katie.display_user_balance()

melissa.transfer_money(thomas, 50)

melissa.display_user_balance()
thomas.display_user_balance()
