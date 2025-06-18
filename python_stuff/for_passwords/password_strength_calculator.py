# Project no. 2 - Password Strength Checker
# This is a CLI based password strength checker made by Ross using Python.

import string

print("\n      -----[Password Strength Checker]-----        ")
print("\nYour password must have atleast 8 letters, an uppercase letter, a number, and a symbol \n")

# Loops until user stops or password is valid
while True:

    # Gets the password
    your_password = input("Enter your password [-1 to exit]: ")

    # Allows user to exit if needed 
    if your_password == "-1":
        break

    # Conditions
    length_checker = 8
    contains_uppercase = any(char.isupper() for char in your_password)
    contains_number = any(char.isdigit() for char in your_password)
    contains_symbols = any(char in string.punctuation for char in your_password)

    # Checking if the password is valid
    if len(your_password) < length_checker:
        print("\nYour password is too short!")
    if not contains_uppercase:
        print("\nYour password must contain atleast one uppercase letter!")
    if not contains_number:
        print("\nYour password must contain atleast one number!")
    if not contains_symbols:
        print("\nYour password must contain atleast one symbol!\n") 

    # Valid password greeting
    if len(your_password) > length_checker and contains_uppercase and contains_number and contains_symbols:
            print("\n-----[Your password is valid and strong!]-----\n")
            break