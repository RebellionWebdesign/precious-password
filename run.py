from time import sleep
import pyfiglet
from simple_term_menu import TerminalMenu
import hashlib


class PasswordCheck():
    def __init__(self, pw_clean, pw_hash, pw_prefix, pw_strength,
                 pw_in_list):
        self.pw_clean = pw_clean
        self.pw_hash = pw_hash
        self.pw_prefix = pw_prefix
        self.pw_strength = pw_strength
        self.pw_in_list = pw_in_list

def ascii_banner():
    banner = pyfiglet.figlet_format("Precious Password",
                                    font="digital",)
    print(banner)

def main_menu():
    options = ["Check password security", "Check database for password",
               "Check if passwordis commonly used", "Quit"]
    main_menu = TerminalMenu(options)
    main_menu_index = main_menu.show()
    print("You have selected {options[main_menu_index]}!")

def main():
    ascii_banner()
    print("Hi and welcome to Precious Password! This app was made to"
          + " help you choosing a safe and secure password."
          + "Check out the options below and choose what you want to"
          + " do")
    main_menu()

if __name__ == "__main__":
    main()
