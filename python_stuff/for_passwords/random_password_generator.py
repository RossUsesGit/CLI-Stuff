# Lets make a random password generator because I'm bored

import random
import string
import time

while True:

    try:
        anata_no_password = int(input("Enter desired password length: "))
        break
    except ValueError:
        print("Error. Invalid password length.")

password_generated = list("*" * anata_no_password)

for i in range(len(password_generated)):
    password_generated[i] = random.choice(string.ascii_letters + string.digits + string.punctuation)

password_generated = ''.join(password_generated)

print("Generating...")
time.sleep(2)
print(f"Your password is: {password_generated}")
print("Stay encrypted!")
