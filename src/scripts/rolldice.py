#! /usr/bin/env python

from random import seed, randint

class Dice:
    """A class that models dice"""
    def __init__(self, sides = 6):
        if (type(sides) != type(0)):
            raise TypeError('# of sides must be an integer')
        if (sides < 1):
            raise IndexError('# of sides must be gt 0')
        self.sides = sides
    
    def roll(self):
        return randint(1, self.sides)

dice = Dice(10)
for i in range(10):
    print('The result of the dice roll was:', dice.roll())
