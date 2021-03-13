from random import randint

class DiceTwenty:
    def __init__ (self, sides=20):
        self.sides = sides

    def roll_twenty(self):
        for sides in range(1,20):
            random = randint(1, 20)
            print(f"The dice rolled a {random}")
    
    

        