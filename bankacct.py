class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self,amount):
        self.amount += amount

    def make_withdraw(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        self.amount += amount
        self.display_user_balance()
        user.display_user_balance()

cassanova = User("cassanova")
alonso = User("alonso")
danny = User("danny")

cassanova.make_deposit(10)
cassanova.make_deposit(200)
cassanova.make_deposit(50)
cassanova.make_withdraw(65)
cassanova.display_user_balance()
# cassanova.transfer_money(50)

alonso.make_deposit(2000)
alonso.make_deposit(3000)
alonso.make_deposit(400)
alonso.make_withdraw(0)
alonso.display_user_balance()

danny.make_deposit(200)
danny.make_deposit(200)
danny.make_deposit(100)
danny.make_withdraw(25)
danny.display_user_balance()