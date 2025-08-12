from enum import Enum
import random   

class Dice(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

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