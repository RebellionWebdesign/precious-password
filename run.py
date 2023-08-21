from time import sleep
from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style
import hashlib, requests, re

#Converts the passwords.txt file to a list
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

#Instance of the class holding password data
pwc_instance = PasswordCheck("", "", "", "NO", "", "")

def get_password():
    user_password = input("Please enter the password you need to check: \n")

    if user_password.strip(" ") == "":
        print("That's not a password. Try again.")
        get_password()
    else:
        pwc_instance.pw_clean = user_password

def check_password_frequency():
    print("\nChecking password frequency...")
    sleep(2)
    if pwc_instance.pw_clean in common_passwords_data:
        print("Password is often used. Not so good.")
        pwc_instance.pw_in_list = "YES"
    else:
        print("Password is not often used. Nice!\n")
        pwc_instance.pw_in_list = "NO"

def hash_password():
    if pwc_instance.pw_clean == "":
        print("Sorry, no password was given\n")
        get_password()
    else:
        pwc_instance.pw_hash = hashlib.sha1(
            bytes(pwc_instance.pw_clean, "utf-8")).hexdigest().upper()
        pwc_instance.pw_prefix = pwc_instance.pw_hash[0:5]
        pwc_instance.pw_suffix = pwc_instance.pw_hash[5:]

def check_password_database():
    print("Checking database for entries...")
    sleep(2)
    request = requests.get("https://api.pwnedpasswords.com/range/"
                           + pwc_instance.pw_prefix)
    
    if request.status_code != 200:
        print("Password doesnt seem to in the database\n")
    else:
        for hash in request.iter_lines():
            stripped_hash = str(hash).strip("b'")
            strip_occur = r":.*"
            stripped_numbers = re.sub(strip_occur, "", stripped_hash)
            complete_hash = stripped_numbers.upper()
            complete_hash.strip()
            hash_list = complete_hash.split("\n")

            if pwc_instance.pw_suffix in hash_list:
                print("Seems like the password was exposed before.\n")
                pwc_instance.pw_in_db = "YES"

def check_password_complexity(*string):
    print("Checking password complexity...")
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
    """ Sets menu options and displays the main menu -> simple mode"""
    menu_options = ["Simple mode (shows simple data)",
                    "Advanced mode (shows advanced data)",
                    "Read manual",
                    "Quit [q or ESC]"]
    menu = TerminalMenu(menu_options)
    menu_index = menu.show()
    menu_quit = False
    print(f"You selected {menu_options[menu_index]}!\n")

    """ This is the menu logic """
    if menu_index == 0:
        get_password()
        hash_password()
        check_password_frequency()
        check_password_database()
        
        if check_password_complexity(pwc_instance.pw_clean):
            print("Password meets the minimum requirements. Great!\n")
        else:
            print("Password doesn´t meet the minimum requirements.\n"
                  "Try to add complexity!\n")
        
        menu.show()
    elif menu_index == 1:
        get_password()
        print("Your password is: " + pwc_instance.pw_clean)
        hash_password()
        print("Your password hash is: " + pwc_instance.pw_hash)
        print("Your password prefix is: " + pwc_instance.pw_prefix)
        print("Your password suffix is: " + pwc_instance.pw_suffix)
        check_password_frequency()
        check_password_database()

        menu.show()
    elif menu_index == 2:
        print("PRECIOUS PASSWORD MANUAL\n"
              "\n"
              "Welcome to PRECIOUS PASSWORD! This program allows users to\n"
              "check if a given password is secure & part of a databreach. \n"
              "You have the following options:\n"
              "\n"
              "SIMPLE MODE:\n"
              "\n"
              "Simple mode only shows easy digestible data related to your\n"
              "given password. This means it only shows if your password\n"
              "is commonly used and if it was hacked before. In addition\n"
              "to that it checks your password for security by determining:\n"
              "\n"
              "-If the password has at least eight characters\n"
              "-If the password has at least one upper case character\n"
              "-If the password has at least one digit [0-9]\n"
              "-If the password has at least one special character [!,?,etc]\n"
              "\n"
              "ADVANCED MODE:\n"
              "\n"
              "Advanced mode does the same as simple mode, but it also shows\n"
              "the resulting SHA-1 hash divided into a prefix and a suffix.\n"
              "The prefix represents the first five digits from the SHA-1\n"
              "hash and is used to check if the prefix is in the database.\n"
              "If the prefix is found, the PWNED PASSSWORD database returns\n"
              "list of suffixes we need toc heck too."
              "The suffix represents the remaining digits of the SHA-1 hash\n"
              "and is used to check the PWNED PASSWORD database. If there\n"
              "is a match between both of them your password is most likely\n"
              "part of a breach and you will need to change it.")
        
        menu.show()
    elif menu_index == 3:
        menu_quit = True
        print("Have a nice day and see you nect time :-)")
        menu.show()
        




if __name__ == "__main__":
    main()
