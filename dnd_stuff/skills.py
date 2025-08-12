from enum import Enum
from dnd_stuff.abilities import Ability

class Skill(Enum):
    ATHLETIC = ("Athletic", Ability.STRENGTH)
    ACROBATICS = ("Acrobatics", Ability.DEXTERITY)
    SLEIGHT_OF_HAND = ("Sleight of Hand", Ability.DEXTERITY)
    STEALTH = ("Stealth", Ability.DEXTERITY)
    ARCANA = ("Arcana", Ability.INTELLIGENCE)
    HISTORY = ("History", Ability.INTELLIGENCE)
    INVESTIGATION = ("Investigation", Ability.INTELLIGENCE)
    NATURE = ("Nature", Ability.INTELLIGENCE)
    RELIGION = ("Religion", Ability.INTELLIGENCE)
    ANIMAL_HANDLING = ("Animal Handling", Ability.WISDOM)
    INSIGHT = ("Insight", Ability.WISDOM)
    MEDICINE = ("Medicine", Ability.WISDOM)
    PERCEPTION = ("Perception", Ability.WISDOM)
    SURVIVAL = ("Survival", Ability.WISDOM)
    DECEPTION = ("Deception", Ability.CHARISMA)
    INTIMIDATION = ("Intimidation", Ability.CHARISMA)
    PERFORMANCE = ("Performance", Ability.CHARISMA)
    PERSUASION = ("Persuasion", Ability.CHARISMA)

    def __init__(self, label, ability):
        self.label = label
        self.ability = ability