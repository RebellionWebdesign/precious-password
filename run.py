## Here we need to import some modules we use
import time ## Time is needed to to have delays for the greeter messages
import hashlib ## This will proide the hash algorithm (SHA-1) for the pwned password api
#import requests ## Requests will handle the http-GET part of the app

class PasswordCheck():
    def __init__(self, pw_clean, pw_hash, pw_prefix, pw_strength, pw_in_list):
        self.pw_clean = pw_clean
        self.pw_hash = pw_hash
        self.pw_prefix = pw_prefix
        self.pw_strength = pw_strength
        self.pw_in_list = pw_in_list

def greeter():
    print("Hi and welcome to Precious Password!")
    time.sleep(5)
    print("With this app you can do the following:\n")
    time.sleep(5)
    print("- Check if your password is secure")
    time.sleep(2)
    print("- Check if your password is in the PWNED PASSWORD database")
    time.sleep(2)
    print("- Check if your password is commonly used")
    time.sleep(2)

def password_input(user_password):
    user_password = input("Please choose a password to test: \n")

    if user_password == "":
        print("Sorry, this is not a password. Try again.")
        password_input()
    else:
        check = PasswordCheck(user_password.upper(), None, None, None, None)
        print(check.pw_clean)

def greeter_input():
    user_response = input("Do you want to enter a password now (y/n)?\n")

    if user_response == "y":
        print("Okay, let´s go!")
        password_input()
    elif user_response == "n":
        print("Have a nice day!")
        exit()
    else:
        print("Please input y or n")
        greeter_input()

greeter()
greeter_input()

