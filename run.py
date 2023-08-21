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
    menu_options = ["Simple mode",
                    "Advanced mode",
                    "Read manual",
                    "Quit"]
    menu = TerminalMenu(menu_options)
    menu_index = menu.show()
    menu_quit = False


    if menu_index == 0:
        print(f"You selected {menu_options[menu_index]}!\n")
        get_password()
        check_password_frequency()
        check_password_database()
        
        if check_password_complexity(pwc_instance.pw_clean):
            print("Password meets the minimum requirements. Great!")
        else:
            print("Password doesnt meet the minimum requirements.\n"
                  "Try to add complexity!")
    

if __name__ == "__main__":
    main()
