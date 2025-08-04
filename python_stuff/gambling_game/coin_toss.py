import random

class CoinToss():

    def __init__(self):

        self.comp_choice = None
        self.face = None
        
    def play(self):
        
        self.comp_choice = random.randint(1,2)
        if self.comp_choice == 1: 
            self.face = "Heads"
        else:
            self.face = "Tails"

        return self.face

        
