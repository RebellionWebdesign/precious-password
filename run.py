# Built in libraries
from time import sleep
# 3rd party libraries
import re
import hashlib
import requests
from consolemenu import *
from os import system, name
from consolemenu.items import *
from colorama import Fore, Back, Style, init

# Initialises the autoreset on newline for colorama
init(autoreset=True)

# Converts the passwords.txt file to a list
common_passwords = open("passwords.txt", "r")
common_passwords_data = common_passwords.read().split("\n")
common_passwords.close()


# Class holding the password data
class PasswordCheck:
    """
    The base class for the program which provides password data storage. 
    """

    def __init__(self, pw_clean, pw_hash, pw_prefix, pw_in_db,
                 pw_in_list, pw_suffix):
        self.pw_clean = pw_clean
        self.pw_hash = pw_hash
        self.pw_prefix = pw_prefix
        self.pw_in_db = pw_in_db
        self.pw_in_list = pw_in_list
        self.pw_suffix = pw_suffix


# Instance of the base class. Used to store and access password data
pwc_instance = PasswordCheck("", "", "", "NO", "", "")


def back_to_main():
    """Sends the user back to the main menu after reading the manual"""
    check_button = input("Press ENTER to go back to the main menu!")

    if check_button == "":
        main()
    else:
        print("Please only press ENTER :-)")
        back_to_main()


def show_manual():
    """Shows the manual if the user wishes to read it"""
    manual_open = open("manual.txt", "r")
    manual_read = manual_open.read()
    manual_open.close()
    clear_screen()
    print(manual_read)

    back_to_main()


def get_password():
    """
    Takes a user password from input(), strips spaces from start and end
    and validates the input. Loops until a valid password is given.
    """
    user_password = input("Please enter the password you need to check: \n")

    if user_password.strip(" ") == "":
        print(Back.RED + "That's not a password. Try again.")
        get_password()
    else:
        pwc_instance.pw_clean = user_password


def check_password_frequency():
    """
    Takes the passwords.txt file and converts it to a list. After the
    user password is recieved it gets compared to the list. if the pass-
    word is in the list the user gets a message, and if not too! 
    """
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
    """
    Checks if the pwc_instance class has a value in pw_clean. If not, no
    password was given and the user gets invited to again to give a
    password. If a password was given, it gets hashed to a SHA-1 check-
    sum for the pwned password api. The SHA.1 checksum gets separated to
    the prefix (first five chars of SHA-1) and the suffix (remaining
    chars from the SHA-1) which get stored in pwc_instance
    """
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
    """
    Takes the SHA-1 prefix from pwc_instance.pw_prefix and sends a GET
    request to the pwned passwords api. The api returns SHA-1 suffixes
    as a list which get stripped (all chars/nums after the colon). Then
    we can compare the previously generated password suffix to the
    passwords list. If a match is found the user gets notified, and if
    not the user gets notified too.
    """
    print("\nChecking database for entries...")
    sleep(2)
    request = requests.get("https://api.pwnedpasswords.com/range/"
                           + pwc_instance.pw_prefix)

    stripping_regex = r":.*"
    stripped_request = re.sub(stripping_regex, "", request.text)

    if request.status_code == 404:
        print(Back.GREEN + "Password doesnt seem to be in the database")

    if pwc_instance.pw_suffix in stripped_request:
        print(Back.RED + "Seems like the password was exposed before.")
        pwc_instance.pw_in_db = "YES"
    else:
        print(Back.GREEN + "Password doesnt seem to be in the database")


def check_password_complexity(*string):
    """
    Checks the given password for complexity by constraining it to at
    least 8 chars, one uppercase, one digit and a special char. Returns
    True only if all checks are true.
    """
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


def exit_program():
    """
    The consolemenu library doesnt provide an interface for printing a
    message when the user quits. So this is a basic custom function to
    do so. 
    """
    exit_question = input("\nAre you sure you want to quit [y/n]?\n")

    if exit_question == "y":
        clear_screen()
        print("\nOkay, have a nice day and see you soon :-)", flush=True)
        sleep(3)
        main()
    elif exit_question == "n":
        clear_screen()
        print("\nOkay, I will restart the program now :-)", flush=True)
        sleep(3)
        main()
    elif exit_question != "y" or "n":
        clear_screen()
        print("\nSorry, thats not the correct key")
        exit_program()


def mode_question():
    """Asks the user if the program mode should be changed.
        Loops until an answer is given."""
    question_mode = input("Do you want to use simple mode, advanced"
                          + " mode or quit [s/a/q]?")

    if question_mode == "s":
        simple_mode()
    elif question_mode == "a":
        advanced_mode()
    elif question_mode == "q":
        exit_program()
    elif question_mode != "s" or "a" or "q":
        mode_question()


def new_test_question():
    """Asks the user if he wants to test another password.
        Loops until an answer is is given."""
    question_simple = input("\nDo you want to test another one [y/n]?\n")

    if question_simple == "n":
        exit_program()
    elif question_simple == "y":
        mode_question()
    elif question_simple != "n" or "y":
        print("Sorry, I dont know that key...", flush=True)
        new_test_question()


def simple_mode():
    """
    This is the "Simple Feedback Mode". It checks the user password
    against all the above functions and notifies the user whether a test
    was passed or not. In addition it invites the user to check
    another password and to maybe change the feedback modes.
    """
    clear_screen()
    print("You selected simple mode")
    get_password()
    hash_password()
    check_password_frequency()

    # This validates the check_password_complexity() function
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

    new_test_question()


def advanced_mode():
    """
    This is the "Advanced Feedback Mode". It basically does the same as
    the simple_mode() function, but adds the SHA-1 checksum, prefix and
    suffix
    """
    clear_screen()
    print("You selected advanced mode")
    sleep(2)
    get_password()
    print("Your password is: " + pwc_instance.pw_clean + "\n")
    hash_password()
    print("Your password hash is: " + pwc_instance.pw_hash + "\n")
    print("Your password prefix is: " + pwc_instance.pw_prefix + "\n")
    print("Your password suffix is: " + pwc_instance.pw_suffix + "\n")
    check_password_frequency()

    # This validates the check_password_complexity() function
    if check_password_complexity(pwc_instance.pw_clean):
        print(Back.GREEN +
              "Password meets the minimum requirements. Great!")
        print()
    else:
        print(Back.RED +
              "Password doesn´t meet the minimum requirements."
              " Try to add complexity!")
        print("[At least 8 characters, one uppercase, one digit and" +
              " one special character!]")

    check_password_database()
    new_test_question()


def clear_screen():
    """
    Clears the screen to have an uncluttered experience after checking
    if the OS used is NT (Windows) or POSIX (Linux/Mac)
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def main_menu():
    """
    Constructs the main menu and displays it.
    """
    menu = ConsoleMenu("Welcome to Precious Password!",
                       " Please type an option and type your password" +
                       " when prompted!", show_exit_option=False)
    menu_item = MenuItem("Menu Item")
    first_item = FunctionItem("Simple Feedback Mode",
                              simple_mode)
    second_item = FunctionItem("Advanced Feedback Mode",
                               advanced_mode)
    third_item = FunctionItem("RTFM [Read The Friendly Manual]",
                              show_manual)
    fourth_item = FunctionItem("Quit", exit_program)

    menu.append_item(first_item)
    menu.append_item(second_item)
    menu.append_item(third_item)
    menu.append_item(fourth_item)
    menu.show()


def main():
    """
    Starts the menu function which handles the other functions
    """
    main_menu()


if __name__ == "__main__":
    """
    This gets executed only, if the code to beexecuted is handled
    directly by python. Doesnt work when we import the file e.g.
    import run.py
    """
    main()
