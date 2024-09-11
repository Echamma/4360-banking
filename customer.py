import json

class Customer():
    def __init__(self, name, accountNumber,password,balance):
        self.name = name
        self.account_number = accountNumber
        self.password = password
        self.balance = int(balance)
        self.counter = 0

    def deposit(self, amountOfMoney):
        if(amountOfMoney > 2000 or amountOfMoney < 0 or self.counter >2):
            print("Invalid Transaction")
        else:
            self.balance += int(amountOfMoney)

    def withdraw(self, amountOfMoney):
        if(amountOfMoney > self.balance or amountOfMoney < 0):
            return "Invalid Transaction"        
        else:
            self.balance -= int(amountOfMoney)

    def to_json(self):

        return {

            "name": self.name,

            "accountNumber": self.accountNumber,

            "password": self.password,

            "balance": self.balance

        }