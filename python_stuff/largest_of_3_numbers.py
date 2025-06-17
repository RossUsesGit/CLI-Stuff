# Create a program that finds the largest number out of 3 numbers

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
num3 = float(input("Please enter the third number: "))

highest = max(num1,num2,num3)

print("The largest number out of the three inputs is",highest)



# It can also be like this (remove the quotation marks ["""])

"""
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
num3 = float(input("Please enter the third number: "))

highest = 0

if num1 > num2 and num1 > num3:
    highest = num1

if num2 > num1 and num2 > num3:
    highest = num2

else:
    highest = num3

print("The largest number out of the three inputs is",highest)

"""