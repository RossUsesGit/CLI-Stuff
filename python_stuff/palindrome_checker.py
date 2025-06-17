# Check if a given string is a palindrome or not.

# Gets the user's input
user_input = str(input("Please enter a word, phrase, or sentence: "))

# Removes any spaces from the user's input
nospace = user_input.replace(" ", "")

# Removes any uppercase letter for easier checking
no_upper = nospace.lower()

# Reverses the string
reversed_string = no_upper[::-1]

# Check if the updated string version is the same as its reverse

if no_upper == reversed_string:
    print(f"{user_input} is a palindrome!")
else:
    print(f" {user_input} is NOT a palindrome.")

