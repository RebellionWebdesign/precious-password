## Here we need to import some modules we use
import time ## Time is needed to to have delays for the greeter messages
#import requests ## Requests will handle the http-GET part of the app

def greeter():
    print("Hi and welcome to Precious Password!")
    time.sleep(5)
    print("With this app you can do the following:")
    time.sleep(5)
    print("- Check if your password is secure")
    time.sleep(2)
    print("- Check if your password is in the PWNED PASSWORD database")
    time.sleep(2)
    print("- Check if your password was hacked previously")
    time.sleep("5")
    greeter_input = input("Do you want to enter a password now (y/n)?\n")

    if greeter_input != "y":
        print("Sorry, you ned to enter y for yes or n for no")
    elif greeter_input != "n":
        print("Sorry, you ned to enter y for yes or n for no")
    elif greeter_input == "n":
        print("Okay, no problem. Have a nice day!")
    else:
        print("Okay, let's go!")

greeter()
