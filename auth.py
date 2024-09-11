from dbmanagement import dbManagement
from customer import Customer

class auth:
    def __init__(self, username, password, db: dbManagement):
        self.username = username
        self.password = password
        self.counter = 0
        self.db = db

    def __counter_check(self):
        if self.counter > 2:
            return False
        return True

    def login(self):
        if not self.__counter_check():
            return "invalid login"
        
        data = self.db.read_file()
        for user in data:
            if user["name"] == self.username and user["password"] == self.password:
                return Customer(user["name"], user["accountNumber"], user["password"],user["balance"])
        self.counter += 1
        return "invalid username or password"   