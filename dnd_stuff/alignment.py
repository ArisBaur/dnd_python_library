from enum import Enum, auto

class Alignment(Enum):
    LAWFUL_GOOD = auto()
    NEUTRAL_GOOD = auto()
    CHAOTIC_GOOD = auto()
    LAWFUL_NEUTRAL = auto()
    TRUE_NEUTRAL = auto()
    CHAOTIC_NEUTRAL = auto()
    LAWFUL_EVIL = auto()
    NEUTRAL_EVIL = auto()
    CHAOTIC_EVIL = auto()

    def __init__(self, label):
        self.label = label