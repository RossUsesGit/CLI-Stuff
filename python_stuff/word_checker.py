# Ask the user for a string and count how many words there are.
# This is a simpler version.

user_input = str(input("Please enter your text: ")) 

word_split = user_input.split()

word_count = 0

for i in range(len(word_split)):
    word_count+=1

print("Your text has",word_count,"words!")
