## Here we need to import some modules we use
import time ## Time is needed to to have delays for the greeter messages
#import requests ## Requests will handle the http-GET part of the app

def greeter():
    print("Hi and welcome to Precious Password!")
    time.sleep(5)
    print("With this app you can do the following:\n")
    time.sleep(5)
    print("- Check if your password is secure")
    time.sleep(2)
    print("- Check if your password is in the PWNED PASSWORD database")
    time.sleep(2)
    print("- Check if your password was hacked previously")
    time.sleep(2)

def greeter_input(*user_response):
    user_response = input("Do you want to enter a password now (y/n)?\n")

    if user_response == "y":
        print("Works!")
    elif user_response == "n":
        print("Have anice day!")
        exit()
    else:
        print("Please input y or n")
        greeter_input()

greeter()
greeter_input()

