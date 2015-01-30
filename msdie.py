#msdie.py
# Class defnition for an n-sided die.

from random import randrange
#saed what is "from" and what is it doing?

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

        #strange - I created an object called die1 = MSDie(6)



die1 = MSDie(6)

def main():
    die1.roll()
    die1.getValue()
    print(die1.getValue())
main()


#Strange when I create the object die1, i define
#it's side attributes to have a value of 6.
#but to try and break it I die1.setValue(7).
#Oddly enough it keeps the value of 7 inspite of having the 6 side
#attributes value.
#To add to the oddity, when I roll, and reroll several times, 7 never
#gets
#Why does die1 take the value of 7, but revert
#to it's defined 6 sides when rolling
