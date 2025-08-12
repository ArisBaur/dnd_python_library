from enum import Enum

class Condition(Enum):
    BLINDED = ("blinded", False)
    CHARMED = ("charmed", False)
    DEAFENED = ("deafened", False)
    FRIGHTENED = ("frightened", False)
    GRAPPLED = ("grappled", False)
    INCAPACITATED = ("incapacitated", False)
    INVISIBLE = ("invisible", False)
    PARALYZED = ("paralyzed", False)
    PETRIFIED = ("petrified", False)
    POISONED = ("poisoned", False)
    PRONE = ("prone", False)
    RESTRAINED = ("restrained", False)
    STUNNED = ("stunned", False)
    UNCONSCIOUS = ("unconscious", False)

    def __init__(self, label, isActive):
        self.label = label
        self.isActive = isActive
