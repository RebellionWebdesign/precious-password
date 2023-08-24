import hashlib
import requests
import re
from time import sleep
from consolemenu import *
from consolemenu.items import *
from os import system, name
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Converts the passwords.txt file to a list
common_passwords = open("passwords.txt", "r")
common_passwords_data = common_passwords.read().split("\n")
common_passwords.close()


# Class holding the password data
class PasswordCheck:
    def __init__(self, pw_clean, pw_hash, pw_prefix, pw_in_db,
                 pw_in_list, pw_suffix):
        self.pw_clean = pw_clean
        self.pw_hash = pw_hash
        self.pw_prefix = pw_prefix
        self.pw_in_db = pw_in_db
        self.pw_in_list = pw_in_list
        self.pw_suffix = pw_suffix


# Instance of the class holding password data
pwc_instance = PasswordCheck("", "", "", "NO", "", "")


def get_password():
    user_password = input("Please enter the password you need to check: \n")

    if user_password.strip(" ") == "":
        print(Back.RED + "That's not a password. Try again.")
        get_password()
    else:
        pwc_instance.pw_clean = user_password


def check_password_frequency():
    print("\nChecking password frequency...")
    sleep(2)
    if pwc_instance.pw_clean in common_passwords_data:
        print(Back.RED + "Password is often used. Not so good.")
        pwc_instance.pw_in_list = "YES"
    else:
        print(Back.GREEN + "Password is not often used. Nice!")
        print()
        pwc_instance.pw_in_list = "NO"


def hash_password():
    if pwc_instance.pw_clean == "":
        print(Back.RED + "Sorry, no password was given")
        print()
        get_password()
    else:
        pwc_instance.pw_hash = hashlib.sha1(
            bytes(pwc_instance.pw_clean, "utf-8")).hexdigest().upper()
        pwc_instance.pw_prefix = pwc_instance.pw_hash[0:5]
        pwc_instance.pw_suffix = pwc_instance.pw_hash[5:]


def check_password_database():
    print("\nChecking database for entries...")
    sleep(2)
    request = requests.get("https://api.pwnedpasswords.com/range/"
                           + pwc_instance.pw_prefix)

    stripping_regex = r":.*"
    stripped_request = re.sub(stripping_regex, "", request.text)

    if pwc_instance.pw_suffix in stripped_request:
        print(Back.RED + "Seems like the password was exposed before.")
    else:
        print(Back.GREEN + "Password doesnt seem to be in the database")


def check_password_complexity(*string):
    print("\nChecking password complexity...")
    sleep(2)
    if len(pwc_instance.pw_clean) < 8:
        return False
    elif not re.search(r"[A-Z]", pwc_instance.pw_clean):
        return False
    elif not re.search(r"[a-z]", pwc_instance.pw_clean):
        return False
    elif not re.search(r"\d", pwc_instance.pw_clean):
        return False
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', pwc_instance.pw_clean):
        return False

    return True


def easy_mode():
    print("You selected easy mode")
    get_password()
    hash_password()
    check_password_frequency()

    if check_password_complexity(pwc_instance.pw_clean):
        print(Back.GREEN +
              "Password meets the minimum requirements. Great!")
    else:
        print(Back.RED +
              "Password doesn´t meet the minimum requirements."
              "Try to add complexity!")
        print("[At least 8 characters, one uppercase, one digit and" +
              " one special character!]")
    check_password_database()

    easy_question = input("\nDo you want to test another one [y/n]?\n")

    if easy_question.strip() == "y":
        easy_mode_question = input("\nDo you want to use easy or" +
                                   "advanced mode [e/a] ?\n")
        if easy_mode_question.strip() == "e":
            clear_screen()
            easy_mode()
        elif easy_mode_question.strip() == "a":
            clear_screen()
            advanced_mode()
        elif easy_mode_question.strip != "e" or "a":
            sleep(1)
            print("Sorry, thats no answer.")
    else:
        main_menu()

def advanced_mode():
    print("You selected advanced mode")
    sleep(2)
    get_password()
    print("Your password is: " + pwc_instance.pw_clean + "\n")
    hash_password()
    print("Your password hash is: " + pwc_instance.pw_hash + "\n")
    print("Your password prefix is: " + pwc_instance.pw_prefix + "\n")
    print("Your password suffix is: " + pwc_instance.pw_suffix + "\n")
    check_password_frequency()

    if check_password_complexity(pwc_instance.pw_clean):
        print(Back.GREEN +
              "Password meets the minimum requirements. Great!")
        print()
    else:
        print(Back.RED +
              "Password doesn´t meet the minimum requirements."
              "Try to add complexity!")
        print("[At least 8 characters, one uppercase, one digit and" +
              " one special character!]")

    check_password_database()
    advanced_question = input("\nDo you want to test another one [y/n]?\n")

    if advanced_question.strip() == "y":
        advanced_mode_question = input("Do you want to use easy or" +
                                       "advanced mode [e/a] ?\n")
        if advanced_mode_question.strip() == "e":
            easy_mode()
        elif advanced_mode_question.strip() == "a":
            advanced_mode()
        elif advanced_mode_question.strip != "e" or "a":
            print("Sorry, thats no answer.")
            sleep(1)
    else:
        main_menu()

def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def main_menu():
    menu = ConsoleMenu("Welcome to Precious Password!",
                       "This is the main menu!")
    menu_item = MenuItem("Menu Item")
    first_item = FunctionItem("Simple Feedback Mode",
                              easy_mode)
    second_item = FunctionItem("Advanced Feedback Mode",
                               advanced_mode)
    third_item = FunctionItem("RTFM [Read The Friendly Manual]",
                              input, ["Enter an input"])

    menu.append_item(first_item)
    menu.append_item(second_item)
    menu.append_item(third_item)
    menu.show()


def main():
    main_menu()


if __name__ == "__main__":
    main()
