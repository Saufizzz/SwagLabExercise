'''class Account:
    Initial_value = 300

    def __init__(self, account_bank):
        self.account_bank = account_bank
        self.deposit_amount = 0  # Initialize deposit_amount in the constructor

    def deposit(self):
        depo = float(input("What's your deposit amount? "))  # Convert input to float
        self.deposit_amount += depo  # Update deposit_amount
        return depo

    def amount_balance(self):
        balance = self.deposit_amount + Account.Initial_value
        return f"In your account {self.account_bank}, you have {balance} as you have deposited {self.deposit_amount}"

# Create an object of the Account class
obj1 = Account("Maybank")

# Call the deposit method
deposited_amount = obj1.deposit()

# Call the amount_balance method and print the result
result = obj1.amount_balance()
print(result) '''

#this is without constructor
class Account:
    Initial_value = 0

    def deposit(self):
        depo = float(input("What's your deposit amount? "))
        self.deposit_amount = depo  # Initialize deposit_amount when deposit is made
        return depo

    def amount_balance(self):
        balance = self.deposit_amount + Account.Initial_value
        return f"In your account, you have {balance} as you have deposited {self.deposit_amount}"

# Create an object of the Account class
obj1 = Account()

# Call the deposit method
deposited_amount = obj1.deposit()

# Call the amount_balance method and print the result
result = obj1.amount_balance()
print(result)
