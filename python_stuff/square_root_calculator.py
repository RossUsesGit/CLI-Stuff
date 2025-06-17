# Ask the user for a number, then calculate that number's square root.

user_number = float(input("Please enter a number: "))

if user_number < 0:
    print("Negative numbers have no square root.")

else:
    square_root = (user_number)**(1/2)
    print("The square root of your number is" , square_root)






