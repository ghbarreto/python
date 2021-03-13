import dice
from random import randint

class TenDice(dice.Dice):
    def __init__(self, sides):
        super().__init__(sides)
        self.sides = 10

    def rollTen(self):
        for side in range(1, 10):
            sides = randint(1, 10)
            print(f"The 10-sided dice rolled a {sides}")

