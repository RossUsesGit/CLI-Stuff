import random

class DiceRoll():
    def __init__(self):
        self.computer_roll = None
        self.user_roll = None
        self.result = None

    def play(self):
        self.computer_roll = random.randint(1,6)
       
        while True:
            try:
                self.user_roll = int(input("Choose a number from 1-6: "))
                if self.user_roll not in [1,2,3,4,5,6]:
                    print("Invalid.")
                else:
                    break
            except ValueError:
                print("Invalid.")
       
        print(f"Computer chose: {self.computer_roll}")
        print(f"You chose: {self.user_roll}")

        if self.user_roll == self.computer_roll:
            self.result = "Win"
        else:
            self.result = "Lose"
           
        print(f"You {self.result}!")

dicerollgame = DiceRoll()
dicerollgame.play()
