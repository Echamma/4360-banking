class Customer():
    def __init__(self, name, accountNumber,password,balance):
        self.name = name
        self.account_number = accountNumber
        self.password = password
        self.balance = int(balance)
        self.counter = 0

    def deposit(self, deposit_amount):
        if(deposit_amount > 2000):
            print("Invalid Transaction: Deposit amount must be less than 2000")
        elif(deposit_amount < 0):
            print("Invalid Transaction: Deposit amount must be more than 0")
        elif(self.counter > 2):
            print("Invalid Transaction: Too many failed login attempts")
        else:
            self.balance += int(deposit_amount)

    def withdraw(self, withdraw_amount):
        if(withdraw_amount > self.balance):
            print("Invalid Transaction: Withdraw amount cannot be more than what's currently in account")
        elif(withdraw_amount < 0):
            print("Invalid Transaction: Withdraw amount must be more than 0")
        else:
            self.balance -= int(withdraw_amount)

    def to_json(self):

        return {

            "name": self.name,

            "accountNumber": self.accountNumber,

            "password": self.password,

            "balance": self.balance

        }