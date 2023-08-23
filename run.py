import hashlib
import requests
import re
import pyfiglet
from time import sleep
from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style, init

ascii_text = pyfiglet.figlet_format("Precious Password")
print(ascii_text)

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

    if request.status_code == 200:
        for hash in request.iter_lines():
            stripped_hash = str(hash).strip("b'")
            strip_occur = r":.*"
            stripped_numbers = re.sub(strip_occur, "", stripped_hash)
            complete_hash = stripped_numbers.upper()
            complete_hash.strip()
            hash_list = complete_hash.split("\n")

    if pwc_instance.pw_suffix in hash_list:
        print(Back.RED +
              "Seems like the password was exposed before.")
        pwc_instance.pw_in_db = "YES"
    else:
        print(Back.GREEN +
              "Password doesnt seem to be in the database")


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


def main():
    main_title = "\nChoose an option. Press q or ESC to quit\n"
    main_options = ["Simple mode (show simple data)",
                    "Advanced mode (show advanced data)",
                    "RTFM (Read The Friendly Manual)",
                    "Quit"]
    main_cursor = "> "
    main_cursor_style = ("fg_red", "bold")
    main_exit = False
    clear_screen = False

    menu = TerminalMenu(
        menu_entries=main_options,
        title=main_title,
        menu_cursor=main_cursor,
        menu_cursor_style=main_cursor_style,
        cycle_cursor=True,
    )

    manual_title = "This is the manual. Press q or ESC to go back."
    manual_items = ["Back to main menu"]
    manual_back = False

    manual_menu = TerminalMenu(
        manual_items,
        title=manual_title,
        menu_cursor=main_cursor,
        menu_cursor_style=main_cursor_style,
    )

    while not main_exit:
        main_select = menu.show()

        if main_select == 0:
            print("You selected simple mode")
            sleep(2)
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

        elif main_select == 1:
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

        elif main_select == 2:

            while not manual_back:
                manual_select = manual_menu.show()
                print("This is a test!")

                if manual_select == 0 or None:
                    manual_back = True
                    

        elif main_select == 3 or main_select is None:
            print("Thanks and have a nice day!")
            main_exit = True


if __name__ == "__main__":
    main()
