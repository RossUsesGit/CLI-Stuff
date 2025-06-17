
# Write a program that prints the numbers from 1 up to the given number by the user.
# For each number, apply the following rules:
# If the number is divisible by 3, print "Fizz" instead.
# If it's divisible by 5, print "Buzz" instead.
# If it's divisible by both 3 and 5, print "FizzBuzz" instead.
# If it's divisible by 7, print "Bang" instead.
# If it's divisible by 3 and 7, print "FizzBang" instead.
# If it's divisible by 5 and 7, print "BuzzBang" instead.
# If it's divisible by 3, 5, and 7, print "FizzBuzzBang" instead.
# If none of the above conditions apply, just print the number.


number = int(input("Please enter a number for the FizzBuzzBang: "))
number = number+1

for i in range(number):
   

    if  i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzBang")

    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0 and i % 7 == 0:
        print("FizzBang")
    
    elif i % 5 == 0 and i % 7 == 0:
        print("BuzzBang")
       
    elif i % 3 == 0:
        print("Fizz")
       
    elif i % 5 == 0:
        print("Buzz")

    elif i % 7 == 0:
        print("Bang")
   
    else: print(i)