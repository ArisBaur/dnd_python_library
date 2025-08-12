from enum import Enum

class Ability(Enum):
    STRENGTH = ("Strength", "STR")
    DEXTERITY = ("Dexterity", "DEX")
    CONSTITUTION = ("Constitution", "CON")
    INTELLIGENCE = ("Intelligence", "INT")
    WISDOM = ("Wisdom", "WIS")
    CHARISMA = ("Charisma", "CHA")

    def __init__(self, label, shorthand):
        self.label = label
        self.shorthand = shorthand
    
    @classmethod
    def score_to_modifier(cls, score):
        if score is None:
            return None
        return (score - 10) // 2

    @classmethod
    def modifier_to_score(cls, modifier):
        if modifier is None:
            return None
        return modifier * 2 + 10