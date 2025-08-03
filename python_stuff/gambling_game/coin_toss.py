"""
main
"""

import random


print("[Games]")
print("Coin Toss [1]")


while True:

    try:
        key = int(input("Play: "))
        break
    except ValueError:
        print("Invalid.")

if key == 1:
    num = random.randint(1,2)
    result = "Null"
    if num == 1:
        result = "Heads"
    else:
        result = "Tails"

    while True:

        try: 
            print("Heads or Tails?")
            print("Heads [1]")
            print("Tails [2]")
            choice = int(input("Play: "))

            if choice > 2 or choice < 1:
                print("Invalid.")
                continue
            elif choice == num:
                print(result)
                print("YOU WON!")
                break
            else: 
                print(result)
                print("YOU LOSE.")
                break
        except ValueError:
            print("Invalid.")
    



    
    
