# Simple Word Filter. Create a function that would accept two inputs: a sentence(string), 
# and a list containing bad words that the user would like to censor but not remove. 
# The function should return the newly filtered sentence wherein the bad words are replaced with asterisks 
# equal to the length of the censored word.

def censor():

    # Get user input
    user_input = input("Enter a word, sentence, or phrase: ")

    # Create an empty list to store words the user wants to censor
    censored_words = []

    while True:
        
        # Enter the items into the censored_words list
        add_item = str(input("\nPlease enter a word you want to censor [-1 to stop]: "))
        
        # Break key; this means that the process of getting inputs will stop
        if add_item == "-1":
            break
        else:
            # Append the item if the item is not the break key
            censored_words.append(add_item)

    # Replace each occurrence of a word in censored_words 
    # found in user_input with asterisks (*) of the same length as the word.
    for word in censored_words:
        user_input = user_input.replace(word, "*" * len(word))

    # Print the final censored sentence
    print(f"\nCensored sentence: {user_input}")

# Execute the function
censor()

    