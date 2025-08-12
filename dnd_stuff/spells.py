
from enum import Enum, Flag

#cantrips are also spells, just level 0
class CastingTime(Enum):
    ACTION = "1 action"
    BONUS_ACTION = "1 bonus action"
    REACTION = "1 reaction"
    ONE_ROUND = "1 round"
    ONE_MINUTE = "1 minute (10 rounds)"
    TEN_MINUTES = "10 minutes"
    ONE_HOUR = "1 hour"
    EIGHT_HOURS = "8 hours"
    VERY_LONG = "oh so long..."

class SpellSchool(Enum):
    ABJURATION = "Abjuration"
    CONJURATION = "Conjuration"
    DIVINATION = "Divination"
    ENCHANTMENT = "Enchantment"
    EVOCATION = "Evocation"
    ILLUSION = "Illusion"
    NECROMANCY = "Necromancy"
    TRANSMUTATION = "Transmutation"

class SpellRange(Enum):
    SELF = "Self"
    TOUCH = "Touch"
    THIRTY_FEET = "30 feet"
    SIXTY_FEET = "60 feet"
    ONETWENTY_FEET = "120 feet"
    THREEHUNDRED_FEET = "300 feet"
    SIGHT = "Sight"
    UNLIMITED = "Unlimited"

class SpellDuration(Enum):
    INSTANTANEOUS = "Instantaneous"
    ROUND = "1 round"
    MINUTE = "1 minute (10 rounds)"
    TEN_MINUTES = "10 minutes"
    HOUR = "1 hour"
    EIGHT_HOURS = "8 hours"
    TWENTYFOUR_HOURS = "24 hours"
    UNTIL_DISPELLED = "Until dispelled"
    SPECIAL = "Special"
    CONCENTRATION_ROUND = "Concentration, up to 1 round"
    CONCENTRATION_MINUTE = "Concentration, up to 1 minute"
    CONCENTRATION_TEN_MINUTES = "Concentration, up to 10 minutes"
    CONCENTRATION_HOUR = "Concentration, up to 1 hour"
    CONCENTRATION_EIGHT_HOURS = "Concentration, up to 8 hours"

class SpellComponent(Flag):
    VERBAL = "V"
    SOMATIC = "S"
    MATERIAL = "M"



class Spell:
    def __init__(self, level, name, description, school=None, casting_time=None, spell_range=None, duration=None, components=None):
        self.name = name
        self.level = level
        self.school = school
        self.description = description
        self.casting_time = casting_time
        self.spell_range = spell_range
        self.duration = duration
        self.components = components

    def __str__(self):
        return f"{self.name}:·\n(Lvl{self.level} {self.school} spell.\nCasting Time: {self.casting_time}\tRange: {self.spell_range}\tDuration: {self.duration}\tComponents: {self.components}\n\n{self.description})"
    
# region CHOOSE YOUR SPELL
ChooseOneCantrip = Spell(
    level=0,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other cantrip."
)
ChooseOneFirstLevel = Spell(
    level=1,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
ChooseOneSecondLevel = Spell(
    level=2,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
ChooseOneThirdLevel = Spell(
    level=3,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
ChooseOneFourthLevel = Spell(
    level=4,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
ChooseOneFifthLevel = Spell(
    level=5,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
ChooseOneSixthLevel = Spell(
    level=6,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
ChooseOneSeventhLevel = Spell(
    level=7,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
ChooseOneEighthLevel = Spell(
    level=8,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
ChooseOneNinthLevel = Spell(
    level=9,
    name="Choose One",
    description="This is a filler Spell, you can replace this with any other first level spell."
)
#endregion


#region CANTRIPS
AcidSplash = Spell(
    level=1,
    name="Acid Splash",
    description="You hurl a bubble of acid. Choose one creature you can see within range. The target must succeed on a Dexterity saving throw or take 1d6 acid damage.",
    casting_time=CastingTime.ACTION,
    spell_range=SpellRange.SIXTY_FEET,
    components=SpellComponent.VERBAL | SpellComponent.SOMATIC,
    duration=SpellDuration.INSTANTANEOUS
)


#endregion