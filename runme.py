import customtkinter
from tkinter import *
import users
import json
from dbmanagement import dbManagement
from customer import Customer
from transfer import Money_Management
from auth import auth
from loginwindow import Login

data = dbManagement()

db = users.users(data)

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x600")

def button_function():
    print("button pressed")

login_window = Login(app, data)

app.mainloop()