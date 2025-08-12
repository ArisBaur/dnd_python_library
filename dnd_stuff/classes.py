import pygame
from dnd_stuff.dice import *
from math import floor
import dnd_stuff.spells as Spells

class WizardFeatures():
    Spellcasting = ("Spellcasting", "As a student of arcane magic, you have a spellbook containing spells that show the first glimmerings of your true power.")
    ArcaneRecovery = ("Arcane Recovery", "You have learned to regain some of your magical energy by studying your spellbook")
    CantripFormulas = ("Cantrip Formulas", "At 3rd level, you have scribed a set of arcane formulas in your spellbook that you can use to formulate a cantrip in your mind.")
    AbilityScoreImprovement = ("Ability Score Improvement", "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.")
    SpellMaster = ("Spell Mastery", "At 18th level, you have achieved such mastery over certain spells that you can cast them at will. Choose a 1st-level wizard spell and a 2nd-level wizard spell that are in your spellbook.")
    SignatureSpells = ("Signature Spells", "When you reach 20th level, you gain mastery over two powerful spells and can cast them with little effort. Choose two 3rd-level wizard spells in your spellbook as your signature spells.")

    def __init__(self, label, description):
        self.label = label
        self.description = description



class Wizard():
    # pygame stuff
    class_sprite_path = "assets/sprites/wizard"
    spell_cooldown_time = 1.5

    #dnd stuff
    hit_dice = Dice.d6
    weapon_proficiencies = ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
    saving_throws_proficiencies = ["Intelligence", "Wisdom"]
    skill_proficiencies = ["Choose from (Arcana, History, Insight, Investigation, Medicine, Religion)", "Choose from (Arcana, History, Insight, Investigation, Medicine, Religion)"]
    equipment = {"quarterstaff or dagger": 1, "a component pouch or arcane focus": 1, "a scholar's pack or an explorer's pack": 1, "a spellbook": 1}
    

    #for leveling up and limiting higher lvl features
    unlocked_features = [WizardFeatures.Spellcasting, WizardFeatures.ArcaneRecovery]
    known_cantrips = [Spells.ChooseOneCantrip, Spells.ChooseOneCantrip, Spells.ChooseOneCantrip]
    first_level_prepared_spells = [Spells.ChooseOneFirstLevel, Spells.ChooseOneFirstLevel]   # {spell_level: [spell_name, ...]}
    second_level_prepared_spells = []
    third_level_prepared_spells = []
    fourth_level_prepared_spells = []
    fifth_level_prepared_spells = []
    sixth_level_prepared_spells = []
    seventh_level_prepared_spells = []
    eighth_level_prepared_spells = []
    ninth_level_prepared_spells = []

    spell_slots = {
        1:  {1: 2},
        2:  {1: 3},
        3:  {1: 4, 2: 2},
        4:  {1: 4, 2: 3},
        5:  {1: 4, 2: 3, 3: 2},
        6:  {1: 4, 2: 3, 3: 3},
        7:  {1: 4, 2: 3, 3: 3, 4: 1},
        8:  {1: 4, 2: 3, 3: 3, 4: 2},
        9:  {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
        10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
        11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1},
        12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1},
        13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1},
        14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1},
        15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},
        16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},
        17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
        18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
        19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
        20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
    }



    @classmethod
    def draw(caller, screen):
        sprites = [
            pygame.image.load(f"{caller.class_sprite_path}_down.png"),
            pygame.image.load(f"{caller.class_sprite_path}_right.png"),
            pygame.image.load(f"{caller.class_sprite_path}_up.png"),
            pygame.image.load(f"{caller.class_sprite_path}_left.png")]
        
        sprite_index = int((caller.direction + 45) // 90) % 4
        caller.sprite = sprites[sprite_index]
        caller.sprite = pygame.transform.scale(caller.sprite, (100 * caller.sprite.get_height()/caller.sprite.get_width(), 100))
        screen.blit(caller.sprite, (caller.player_pos.x - caller.sprite.get_width() / 2, caller.player_pos.y - caller.sprite.get_height() / 2))

