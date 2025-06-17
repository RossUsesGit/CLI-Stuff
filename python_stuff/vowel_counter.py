# Ask the user for a word or a sentence. Count how many vowels it contains.

vowels = ['a','e','i','o','u','A','E','I','O','U']

user_input = str(input("Please enter a word or a sentence: "))

user_input = user_input.replace(" " , "")

vowelcount = 0

for i in range(len(user_input)):
    if user_input[i] in vowels:
        vowelcount += 1
    

print("Your input has", vowelcount ,"vowels!")
       





       