class Customer():
    def __init__(self, name, accountNumber,password,balance):
        self.name = name
        self.account_number = accountNumber
        self.password = password
        self.balance = int(balance)
        self.counter = 0

    def deposit(self, deposit_amount):
        if(deposit_amount > 2000 or deposit_amount < 0 or self.counter > 2):
            print("Invalid Transaction")
        else:
            self.balance += int(deposit_amount)

    def withdraw(self, withdraw_amount):
        if(withdraw_amount > self.balance or withdraw_amount < 0):
            return "Invalid Transaction"        
        else:
            self.balance -= int(withdraw_amount)

    def to_json(self):

        return {

            "name": self.name,

            "accountNumber": self.accountNumber,

            "password": self.password,

            "balance": self.balance

        }