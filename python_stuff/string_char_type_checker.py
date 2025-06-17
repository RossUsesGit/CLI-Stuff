# Ask the user for a string, and check if there is an uppercase, lowercase, or a number.

your_string = str(input("Please enter a word, phrase, or a sentence: "))

updated_string = your_string.replace(" ", "")

any_uppercase = any(char.isupper() for char in updated_string)
any_lowercase = any(char.islower() for char in updated_string)
any_numbers = any(char.isdigit() for char in updated_string)

print("Upppercase Checker: ", any_uppercase)
print("Lowercase Checker: ", any_lowercase)
print("Digit Checker: ", any_numbers)



