import pyfiglet
from simple_term_menu import TerminalMenu
import hashlib
import requests
import re

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
pwc_instance = PasswordCheck("", "", "", "", "", "")

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

def hash_password():
    if pwc_instance.pw_clean == "":
        print("Sorry, no password was given")
        get_password()
    else:
        pwc_instance.pw_hash = hashlib.sha1(bytes(pwc_instance.pw_clean, "utf-8")).hexdigest().upper()
        pwc_instance.pw_prefix = pwc_instance.pw_hash[0:5]
        pwc_instance.pw_suffix = pwc_instance.pw_hash[5:]

def check_password_database():
    request = requests.get("https://api.pwnedpasswords.com/range/" + pwc_instance.pw_prefix)
    
    if request.status_code != 200:
        print("Password doesnt seem to in the database")
        pwc_instance.pw_in_db = "NO"
    else:
        print(request.iter_lines())
        for hash in request.iter_lines():
            stripped_hash = str(hash).strip("b'")
            strip_occur = r":.*"
            stripped_numbers = re.sub(strip_occur, "", stripped_hash)
            complete_hash = stripped_numbers.upper()
            complete_hash.strip()
            hash_list = complete_hash.split("\n")

            if pwc_instance.pw_suffix in hash_list:
                print("Seems like the password was exposed before.")
                pwc_instance.pw_in_db = "YES"
            else:
                pwc_instance.pw_in_db = "NO"

def main():
    get_password()
    check_password_frequency()
    hash_password()
    check_password_database()
    print("Given password: " + pwc_instance.pw_clean)
    print("SHA-1: " + pwc_instance.pw_hash)
    print("API search parameter: " + pwc_instance.pw_prefix)
    print("Password found in db: " + pwc_instance.pw_in_db)
    print("Password is commonly used: " + pwc_instance.pw_in_list)
    print("API search response: " + pwc_instance.pw_suffix)

if __name__ == "__main__":
    main()
