from customer import Customer

class Money_Management:

    def __init__(self, user1: Customer, user2: Customer):
        self.user1 = user1
        self.user2 = user2

    def transfer_money(self,amount):
        self.user1.withdraw(amount)
        self.user2.deposit(amount)