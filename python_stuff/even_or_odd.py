# Ask the user for a number and check if that number is odd or even.

your_number = int(input("Please enter a number: "))

if your_number % 2 == 0:
    print(f"{your_number} is an even number!")
else:
    print(f"{your_number} is an odd number!")