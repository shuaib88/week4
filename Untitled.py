#msdie.py
# Class defnition for an n-sided die.

from random import randrange
#saed what is from and what is it doing?

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

        #This is the constructor it defines how you contstruct a new object

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value 
