import random

class RockPaperScissors():
    def __init__(self):
        self.computer_hand = None
        self.user_hand = None
        self.result = None
    
    def play(self):
        print("Rock Paper Scissors")
        print("Enter a hand: ")
        print("[1] Rock")
        print("[2] Paper")
        print("[3] Scissors")

        while True: 

            try:
                self.user_hand = int(input("Your choice: "))
                self.computer_hand = random.randint(1,3)
                if self.user_hand not in [1,2,3]:
                    print("Invalid choice.")
                else:
                    break
            except ValueError:
                print("Invalid.")

        print(f"You chose: {self.user_hand}")
        print(f"Computer chose: {self.computer_hand}")
        
        if self.computer_hand == self.user_hand:
            self.result = "Tie"
        elif self.computer_hand == 1 and self.user_hand == 2:
            self.result = "Win"
        elif self.computer_hand == 2 and self.user_hand == 3:
            self.result = "Win"
        elif self.computer_hand == 3 and self.user_hand == 1:
            self.result = "Win"
        else: 
            self.result = "Lose"

        if self.result == "Tie":
            print("It's a tie!")
        else:
         print(f"You {self.result}!")
        

rpsgame = RockPaperScissors()
rpsgame.play()
