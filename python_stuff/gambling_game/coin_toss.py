import random

class CoinToss():

    def __init__(self):

        self.comp_face = None
        self.user_face = None
        self.result = None
        
    def play(self):
        
        self.comp_choice = random.randint(1,2)
        if self.comp_choice == 1: 
            self.face = "Heads"
        else:
            self.face = "Tails"

        if self.comp_face == self.user_face:
            self.result = "Win"
        else: 
            self.result = "Lose"

        print(f"You {self.result}! ")


        
