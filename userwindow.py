import customtkinter as ctk
from transfer import Money_Management
from customer import Customer

class user_window:
    def __init__(self, name, balance, account_number, app, data):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.app = app
        self.data = data
        self.transfer_attempts = 0
        self.toplevel = ctk.CTkToplevel(width=500, height=500)
        self.frame = ctk.CTkFrame(self.toplevel)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)
        label = ctk.CTkLabel(self.frame, text='Name: ' + self.name, width=40, height=28, fg_color='transparent')
        label.pack(pady=10)
        self.balance_label = ctk.CTkLabel(self.frame, text='Balance: ' + str(self.balance), width=40, height=28, fg_color='transparent')
        self.balance_label.pack(pady=10)
        label = ctk.CTkLabel(self.frame, text='Account Number: ' + str(self.account_number), width=40, height=28, fg_color='transparent')
        label.pack(pady=10)

        # Create a frame for buttons
        button_frame = ctk.CTkFrame(self.frame)
        button_frame.pack(pady=20)

        # Create buttons
        transfer_button = ctk.CTkButton(button_frame, text='Transfer Money', width=140, height=28, command=self.transfer_money)
        transfer_button.pack(side=ctk.LEFT, padx=10)

        add_button = ctk.CTkButton(button_frame, text='Add Money', width=140, height=28, command=self.add_money)
        add_button.pack(side=ctk.LEFT, padx=10)

        withdraw_button = ctk.CTkButton(button_frame, text='Withdraw Money', width=140, height=28, command=self.withdraw_money)
        withdraw_button.pack(side=ctk.LEFT, padx=10)

    def run(self):
        self.toplevel.mainloop()

    def transfer_money(self):
        if self.transfer_attempts > 2:
            print("You have exceeded the maximum number of transfer attempts.")
            return
        # Create a new window for transfer money
        transfer_window = ctk.CTkToplevel(width=300, height=200)
        transfer_window.title('Transfer Money')

        # Create a label and entry for account number
        label = ctk.CTkLabel(transfer_window, text='Enter Account Number:')
        label.pack(pady=10)
        account_number_entry = ctk.CTkEntry(transfer_window, width=200, height=28)
        account_number_entry.pack(pady=10)

        # Create a label and entry for amount
        label = ctk.CTkLabel(transfer_window, text='Enter Amount:')
        label.pack(pady=10)
        amount_entry = ctk.CTkEntry(transfer_window, width=200, height=28)
        amount_entry.pack(pady=10)

        # Create a button to transfer money
        transfer_button = ctk.CTkButton(transfer_window, text='Transfer', width=140, height=28, command=lambda: self.transfer(account_number_entry, amount_entry, transfer_window))
        transfer_button.pack(pady=10)

    def add_money(self):
        # Create a new window for add money
        add_window = ctk.CTkToplevel(width=300, height=200)
        add_window.title('Add Money')

        # Create a label and entry for amount
        label = ctk.CTkLabel(add_window, text='Enter Amount:')
        label.pack(pady=10)
        amount_entry = ctk.CTkEntry(add_window, width=200, height=28)
        amount_entry.pack(pady=10)

        # Create a button to add money
        add_button = ctk.CTkButton(add_window, text='Add', width=140, height=28, command=lambda: self.deposit(amount_entry, add_window))
        add_button.pack(pady=10)

    def withdraw_money(self):
        # Create a new window for withdraw money
        withdraw_window = ctk.CTkToplevel(width=300, height=200)
        withdraw_window.title('Withdraw Money')

        # Create a label and entry for amount
        label = ctk.CTkLabel(withdraw_window, text='Enter Amount:')
        label.pack(pady=10)
        amount_entry = ctk.CTkEntry(withdraw_window, width=200, height=28)
        amount_entry.pack(pady=10)

        # Create a button to withdraw money
        withdraw_button = ctk.CTkButton(withdraw_window, text='Withdraw', width=140, height=28, command=lambda: self.withdraw(amount_entry, withdraw_window))
        withdraw_button.pack(pady=10)

    def update_balance_labels(self):
        self.balance_label.destroy()
        self.balance_label = ctk.CTkLabel(self.frame, text='Balance: ' + str(self.balance), width=40, height=28, fg_color='transparent')
        self.balance_label.pack(pady=10)

    def transfer(self, account_number_entry, amount_entry, transfer_window):
        account_number = account_number_entry.get()
        amount = amount_entry.get()
        if not account_number or not amount:
            print("Please enter both account number and amount")
            self.transfer_attempts += 1
            transfer_window.destroy()
            return
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid amount")
            self.transfer_attempts += 1
            transfer_window.destroy()
            return
        if amount > 2000 or amount < 0:
            print("Invalid transaction. Amount must be between 0 and 2000.")
            self.transfer_attempts += 1
            transfer_window.destroy()
            return
        data = self.data.read_file()
        for user in data:
            if user["accountNumber"] == account_number:
                if amount > self.balance:
                    print("Insufficient balance")
                    self.transfer_attempts += 1
                    transfer_window.destroy()
                    return
                transfer = Money_Management(Customer(self.name, self.account_number, "", self.balance), Customer(user["name"], user["accountNumber"], user["password"], user["balance"]))
                transfer.transfer_money(amount)
                self.data.update_customer(self.account_number, {"balance": self.balance - amount})
                self.data.update_customer(account_number, {"balance": user["balance"] + amount})
                self.balance -= amount
                self.update_balance_labels()
                self.transfer_attempts = 0
                transfer_window.destroy()
                return
        print("Invalid account number")
        self.transfer_attempts += 1
        transfer_window.destroy()

    def deposit(self, amount_entry, add_window):
        amount = amount_entry.get()
        if not amount:
            print("Please enter amount")
            add_window.destroy()
            return
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid amount")
            add_window.destroy()
            return
        if amount > 2000 or amount < 0:
            print("Invalid transaction. Amount must be between 0 and 2000.")
            add_window.destroy()
            return
        self.balance += amount
        self.data.update_customer(self.account_number, {"balance": self.balance})
        self.update_balance_labels()
        add_window.destroy()

    def withdraw(self, amount_entry, withdraw_window):
        amount = amount_entry.get()
        if not amount:
            print("Please enter amount")
            withdraw_window.destroy()
            return
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid amount")
            withdraw_window.destroy()
            return
        if amount > self.balance or amount < 0:
            print("Invalid transaction")
            withdraw_window.destroy()
            return
        if amount > 2000:
            print("Invalid transaction. Amount must be between 0 and 2000.")
            withdraw_window.destroy()
            return
        self.balance -= amount
        self.data.update_customer(self.account_number, {"balance": self.balance})
        self.update_balance_labels()
        withdraw_window.destroy()