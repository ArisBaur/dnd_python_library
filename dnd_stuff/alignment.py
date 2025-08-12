from enum import Enum

class Alignment(Enum):
    LAWFUL_GOOD = "LG"
    NEUTRAL_GOOD = "NG"
    CHAOTIC_GOOD = "CG"
    LAWFUL_NEUTRAL = "LN"
    TRUE_NEUTRAL = "TN"
    CHAOTIC_NEUTRAL = "CN"
    LAWFUL_EVIL = "LE"
    NEUTRAL_EVIL = "NE"
    CHAOTIC_EVIL = "CE"

    def __init__(self, label):
        self.label = label