# declare a class and give it name User
class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

    # adding the withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.name, guido.account_balance)	# output: 300
print(monty.name, monty.account_balance)	# output: 50

guido.make_withdrawal(50)
monty.make_withdrawal(10)
print(guido.name, guido.account_balance)	
print(monty.name, monty.account_balance)	




