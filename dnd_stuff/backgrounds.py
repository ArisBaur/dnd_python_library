from enum import Enum
from dnd_stuff.wallet import Wallet
from dnd_stuff.skills import Skill

class Background(Enum):
    ACOLYTE = ("Acolyte",
               "You have spent your life in the service of a temple to a specific god or pantheon of gods. You act as an intermediary between the realm of the holy and the mortal world, performing sacred rites and offering sacrifices in order to conduct worshipers into the presence of the divine. You are not necessarily a cleric—performing sacred rites is not the same thing as channeling divine power.",
                [Skill.INSIGHT, Skill.RELIGION],
                ["choose", "choose"],
                {"A holy symbol(a gift to you when you entered the priesthood)" : 1, "a prayer book or prayer wheel" : 1, "stick of incense" : 5, "set of vestments" : 1, "set of common clothes" : 1, "belt puch" : 1},
                [0, 15, 0, 0],
                [])

    def __init__(self, label, description, skill_proficiencies, languages, starting_equipment, starting_currency, feats):
        self.label = label
        self.description = description
        self.skill_proficiencies = skill_proficiencies
        self.languages = languages
        self.starting_equipment = starting_equipment
        self.starting_currency = Wallet(starting_currency)
        self.feats = feats
