from time import sleep
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


    

def main():


if __name__ == "__main__":
    main()
