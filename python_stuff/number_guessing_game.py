import random

while True:

    guess = int(input("Guess a number between 1 and 5 [-1 to exit]: "))
    computer_chose = random.randint(1,5)

    if guess == -1:
        break
    
    elif guess > 5 or guess < 1:
        print("Invalid guess.")
    
    elif guess == computer_chose:
        print("Wow! you guessed what the computer was thinking!")
    
    else:
        print("Too bad. Try again?")
    

    