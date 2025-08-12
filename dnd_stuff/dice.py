from enum import Enum
import random   

class Dice(Enum):
    d4 = (4, 2.5, 3)
    d6 = (6, 3.5, 4)
    d8 = (8, 4.5, 5)
    d10 = (10, 5.5, 6)
    d12 = (12, 6.5, 7)
    d20 = (20, 10.5, 11)
    d100 = (100, 50.5, 51)

    def __init__(self, faces, average, rounded_average):
        self.faces = faces
        self.average = average

def roll(faces):
    return random.randint(1, faces)

def d4():
    return roll(Dice.d4.value)

def d6():
    return roll(Dice.d6.value)

def d8():
    return roll(Dice.d8.value)

def d10():
    return roll(Dice.d10.value)

def d12():
    return roll(Dice.d12.value)

def d20():
    return roll(Dice.d20.value)

def d100():
    return roll(Dice.d100.value)