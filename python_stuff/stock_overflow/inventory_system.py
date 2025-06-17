import os
import time
import hashlib
from getpass import getpass

class Item:
    def __init__(self, serial_num, name, quantity, expiry_date, price):
        self.serial_num = serial_num
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.price = price

    def __str__(self):
        return f"Serial Number: {self.serial_num} || Name: {self.name} || Quantity: {self.quantity} || Expiry Date: {self.expiry_date} || Price: {self.price}"

    def to_line(self):
        return f"{self.serial_num},{self.name},{self.quantity},{self.expiry_date},{self.price}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        return Item(parts[0], parts[1], int(parts[2]), parts[3], float(parts[4]))

inventory = []

# === File operations ===
inventory_file = "inventory.txt"
accounts_file = "accounts.txt"

def load_inventory():
    if not os.path.exists(inventory_file):
        return
    with open(inventory_file, 'r') as file:
        for line in file:
            if line.strip():
                inventory.append(Item.from_line(line))

def save_inventory():
    with open(inventory_file, 'w') as file:
        for item in inventory:
            file.write(item.to_line() + "\n")

# === Login System ===
def signup():
    # Count existing accounts
    account_num = 1
    if os.path.exists(accounts_file):
        with open(accounts_file, 'r') as f:
            account_num = sum(1 for line in f if line.startswith("Account #")) + 1

    email = input("Enter email address: ").strip()

    # Email validation
    if "@" not in email or "." not in email:
        print("Invalid email format.\n")
        return False

    # Check if email exists
    if is_email_registered(email):
        print("Email already registered.\n")
        return False

    # Password handling
    while True:
        pswrd = getpass("Enter password: ")
        conf_pswrd = getpass("Confirm password: ")
        if pswrd != conf_pswrd:
            print("Passwords do not match.\n")
        else:
            break

    # Hash and save
    hashpswrd = hashlib.md5(pswrd.encode()).hexdigest()

    # Append and Format
    with open(accounts_file, "a") as f:
        f.write(f"Account #{account_num}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Password: {hashpswrd}\n")
        f.write("---------\n")

    print(f"\nRegistration successful! \n")
    return True

def is_email_registered(email):
# Checks if email exists
    if not os.path.exists(accounts_file):
        return False

    with open(accounts_file, 'r') as f:
        for line in f:
            if line.startswith("Email:"):
                stored_email = line.split("Email:")[1].strip()
                if email.lower() == stored_email.lower():
                    return True
    return False

def login():
# Handles user login with attempts
    email = input("Enter email: ").strip()
    pswrd = getpass("Enter password: ")

    if authenticate_login(email, pswrd):
        print("\nLogin successful!\n")
        return True
    else:
        print("\nInvalid credentials.\n")
        return False

def authenticate_login(email, password):
# Verifies login credentials
    if not os.path.exists(accounts_file):
        return False

    auth_hash = hashlib.md5(password.encode()).hexdigest()
    current_email = None

    with open(accounts_file, 'r') as f:
        for line in f:
            if line.startswith("Email:"):
                current_email = line.split("Email:")[1].strip()
            elif line.startswith("Password:") and current_email:
                stored_hash = line.split("Password:")[1].strip()
                if email.lower() == current_email.lower() and auth_hash == stored_hash:
                    return True
                current_email = None
    return False

def account_system():
    """Main account system interface"""
    while True:
        print("\n==== Account System ====")
        print("1. Sign up")
        print("2. Log in")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            if signup():
                return True  # Proceed after successful signup
        elif choice == "2":
            if login():
                return True  # Proceed after successful login
        elif choice == "3":
            return False  # Exit program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# === Main features ===
def additem():
    while True:
        sn = input("Enter Serial Number: ")
        name = input("Enter Name: ")

        while True:
            try:
                qt = int(input("Enter Quantity: "))
                break
            except ValueError:
                print("Invalid Quantity Unit.")

        exp_date = input("Enter Expiry Date (DD/MM/YYYY): ")

        while True:
            try:
                price = float(input("Enter Price: "))
                break
            except ValueError:
                print("Invalid Price Unit.")

        item = Item(sn, name, qt, exp_date, price)
        inventory.append(item)
        save_inventory()

        while True:
            key = input("Add more? [Y/N]: ").lower()
            if key == 'y':
                break
            elif key == 'n':
                return
            else:
                print('Invalid Key.')

def display_main_menu():
    print("\n===== Menu =====")
    print("[1] Add Item")
    print("[2] View Item")
    print("[3] Update Stock")
    print("[4] Update Price")
    print("[5] Delete Item")
    print("[6] Search Item")
    print("[7] Exit")
    print("==========")

def display_items():
    if inventory:
        print("\n=====[Inventory]=====")
        for item in inventory:
            print(item)
    else:
        print("\nNo items in inventory!")

def display_exit_msg():
    print("\nThank you for using Stock Overflow! [ ^ _ ^ ] ")

def title_block():
    title = """
  _____ ______   ___      __  __  _       ___   __ __    ___  ____   _____  _       ___   __    __
 / ___/|      T /   \    /  ]|  l/ ]     /   \ |  T  |  /  _]|    \ |     || T     /   \ |  T__T  T
(   \_ |      |Y     Y  /  / |  ' /     Y     Y|  |  | /  [_ |  D  )|   __j| |    Y     Y|  |  |  |
 \__  Tl_j  l_j|  O  | /  /  |    \     |  O  ||  |  |Y    _]|    / |  l_  | l___ |  O  ||  |  |  |
 /  \ |  |  |  |     |/   \_ |     Y    |     |l  :  !|   [_ |    \ |   _] |     T|     |l  `  '  !
 \    |  |  |  l     !\     ||  .  |    l     ! \   / |     T|  .  Y|  T   |     |l     ! \      /
  \___j  l__j   \___/  \____jl__j\_j     \___/   \_/  l_____jl__j\_jl__j   l_____j \___/   \_/\_/
"""
    for char in title:
        print(char, end='', flush=True)
        time.sleep(0.0005)

def update_stock():
    try:
        if not inventory:
            print("\nNo items in the inventory.")
            return

        display_items()
        serial_num = input("\nEnter Serial Number: ")
        item = next((item for item in inventory if item.serial_num == serial_num), None)

        if item is None:
            print("\nNo such item found.")
        else:
            while True:
                try:
                    new_stock = int(input("Value of New Stock: "))
                    item.quantity = new_stock
                    save_inventory()
                    print("Stock updated successfully.")
                    break
                except ValueError:
                    print("Invalid Stock Unit.")
    except Exception as error:
        print(f"\nError: {error}")

def update_price():
    if not inventory:
        print("\nNo items in the inventory.")
        return

    display_items()
    serial_num = input("\nEnter Serial Number: ")
    item = next((item for item in inventory if item.serial_num == serial_num), None)

    if item is None:
        print("\nNo such item found.")
    else:
        while True:
            try:
                new_price = float(input("Enter New Price: "))
                item.price = new_price
                save_inventory()
                print("\nPrice updated successfully.")
                break
            except ValueError:
                print("Invalid Price Unit.")

def delete_item():
    if not inventory:
        print("\nNo items in inventory.")
        return

    display_items()
    serial_num = input("\nEnter Serial Number of item to delete: ")
    item = next((item for item in inventory if item.serial_num == serial_num), None)

    if item:
        inventory.remove(item)
        save_inventory()
        print("\nItem deleted successfully.")
    else:
        print("\nItem not found.")

def find_item():
    if not inventory:
        print("\nNo items in inventory.")
        return

    serial_num = input("\nEnter Serial Number: ")
    item = next((item for item in inventory if item.serial_num == serial_num), None)

    if item is None:
        print("\nNo such item found.")
    else:
        print("\n" + str(item))

# ========== MAIN PROGRAM ==========
def main():
    load_inventory()
    title_block()

    # Require login before accessing inventory
    if not account_system():
        display_exit_msg()
        return

    while True:
        display_main_menu()

        while True:
            try:
                mm_key = int(input("\nEnter Key: "))
                if 1 <= mm_key <= 7:
                    break
                else:
                    print("Invalid Key. Please enter a number between 1-7.")
            except ValueError:
                print("Invalid Key. Please enter a number.")

        if mm_key == 1:
            additem()
        elif mm_key == 2:
            display_items()
        elif mm_key == 3:
            update_stock()
        elif mm_key == 4:
            update_price()
        elif mm_key == 5:
            delete_item()
        elif mm_key == 6:
            find_item()
        elif mm_key == 7:
            display_exit_msg()
            break

if __name__ == "__main__":
    main()