import pyfiglet
from simple_term_menu import TerminalMenu
import hashlib

#Converts the passwords.txt file to a list
common_passwords = open("passwords.txt", "r")
common_passwords_data = common_passwords.read()
common_passwords_data.split("\n")
common_passwords.close()

# Class holding the password data
class PasswordCheck:
    def __init__(self, pw_clean, pw_hash, pw_prefix, pw_strength,
                 pw_in_list):
        self.pw_clean = pw_clean
        self.pw_hash = pw_hash
        self.pw_prefix = pw_prefix
        self.pw_strength = pw_strength
        self.pw_in_list = pw_in_list

#Instance of the class holding password data
pwc_instance = PasswordCheck("", "", "", "", "")

def get_password():
    user_password = input("Please enter the password you need to check: \n")

    if user_password.strip() == "":
        print("That's not a password. Try again.")
        get_password()
    else:
        pwc_instance.pw_clean = user_password

def check_password_frequency():
    print("Checking password frequency...")

    if pwc_instance.pw_clean in common_passwords_data:
        print("Password is often used. Not so good.")
        pwc_instance.pw_in_list = "YES"
    else:
        print("Password is not often used. Nice!")
        pwc_instance.pw_in_list = "NO"

def main():
    get_password()
    check_password_frequency()

if __name__ == "__main__":
    main()
