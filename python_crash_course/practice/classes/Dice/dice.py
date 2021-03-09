from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = 6

    def roll(self):    
        for side in range(1, 10):
            randomSide = randint(1, 6)
            print(f"A dice has {randomSide} sides")

