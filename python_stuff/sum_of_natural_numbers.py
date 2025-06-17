# Ask the user for a number, then compute the sum from 1 to that number.

user_number = int(input("Please enter a number: "))
total_sum = 0

for i in range(user_number):
    total_sum += i+1

print("The total sum from 1 to your number is" , total_sum)
