import customtkinter
from tkinter import *
import users
import json
from dbmanagement import dbManagement
from customer import Customer
from transfers import Money_Management
from auth import auth
from userwindow import user_window

class Login:
    def __init__(self, app, data):
        self.data = data
        self.app = app
        self.auth = auth("", "", data)  # Create the auth instance with empty username and password
        self.frame = customtkinter.CTkFrame(app, width=400, height=400)
        self.frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.label = customtkinter.CTkLabel(self.frame, text='User Name', width=40, height=28, fg_color='transparent')
        self.label.pack()
        self.name_input = customtkinter.CTkEntry(self.frame, placeholder_text='User Name', width=140, height=28)
        self.name_input.pack()
        self.label = customtkinter.CTkLabel(self.frame, text='Password', width=40, height=28, fg_color='transparent')
        self.label.pack()
        self.pass_input = customtkinter.CTkEntry(self.frame, placeholder_text='Password', width=140, height=28, show="*")
        self.pass_input.pack()

        self.login_button = customtkinter.CTkButton(master=self.frame, text="login", command=self.login)
        self.login_button.pack(pady=6)
        self.error_label = customtkinter.CTkLabel(self.frame, text='', width=40, height=28, fg_color='transparent')
        self.error_label.pack()

    def login(self):
        name = self.name_input.get()
        password = self.pass_input.get()
        self.auth.username = name  # Update the username and password
        self.auth.password = password
        authentication = self.auth.login()  # Use the existing auth instance
        if authentication == "invalid login" or authentication == "invalid username or password":
            self.error_label.configure(text=authentication)
        else:
            self.frame.destroy()
            user_window(authentication.name, authentication.balance, authentication.account_number, self.app, self.data).run()