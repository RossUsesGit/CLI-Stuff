# Ask the user for a number, then calculate that number's factorial

user_number = int(input("Please enter a number: "))
factorial = 1

if user_number == 0:
    factorial = 1

for i in range(user_number):
    factorial *= i+1

print("The factorial of your number is" , factorial)
