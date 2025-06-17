# Create a list, and check if any number is greater than 10.
# This applies the "any()" function.

list_of_numbers = []
while True:
    number_add = int(input("Enter a number, for as much as you like [-143 to exit]: "))
    list_of_numbers.append(number_add)

    if number_add == -143:
        break


greater = any(i> 10 for i in list_of_numbers)

if greater == True:
    print("There is a number greater than 10!")
else:
    print("There is no number greater than 10 :( ")

