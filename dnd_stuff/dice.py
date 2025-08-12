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
    return roll(4)

def d6():
    return roll(6)

def d8():
    return roll(8)

def d10():
    return roll(10)

def d12():
    return roll(12)

def d20():
    return roll(20)

def d100():
    return roll(100)