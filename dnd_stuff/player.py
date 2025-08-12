import pygame
from dnd_stuff.conditions import Condition
from math import sin, cos, radians, floor

from dnd_stuff.wallet import Wallet


# the paradigmn of composition makes more sense
# player has a race and a class
# player isn't a class and it isn't a race
class Player:
    def __init__(self, name, level, dnd_class, race, background, alignment, strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None):
        #sfml and gameplay stuff
        self.player_pos = pygame.Vector2(640, 360)
        self.player_velocity = pygame.Vector2(0, 0)
        self.direction = 180
        self.class_sprite_path = None
        self.race_sprite_path = None
        self.cast_cooldown = None
        self.spell_cooldown_time = None

        #dnd stuff, those initialized to None will be set in the class/race
        self.name = name
        self.dnd_class = dnd_class
        self.level = min(level, 20)
        self.background = background
        self.race = race
        self.alignment = alignment
        self.ability_scores = {
            "strength": strength,
            "dexterity": dexterity,
            "constitution": constitution,
            "intelligence": intelligence,
            "wisdom": wisdom,
            "charisma": charisma
        }
        self.proficiency_bonus = floor(0.25*level - 0.125) + 2
        self.armor_class = 10 + self.ability_scores["dexterity"]
        self.initiative = self.ability_scores["dexterity"]
        self.speed = race.speed
        self.hit_dice = dnd_class.hit_dice
        if self.level == 1:
            self.max_hit_points = self.hit_dice.faces + self.ability_scores["constitution"]
        else:
            self.max_hit_points = self.hit_dice.rounded_average*self.level + self.ability_scores["constitution"]
        self.hit_points = self.max_hit_points
        self.hit_dice_count = self.level
        self.death_saves = {"success": 0, "failure": 0}
        self.armor_proficiencies = list(set(self.armor_proficiencies) | set(dnd_class.armor_proficiencies))
        self.weapon_proficiencies = list(set(self.weapon_proficiencies) | set(dnd_class.weapon_proficiencies))
        self.tool_proficiencies = list(set(self.tool_proficiencies) | set(dnd_class.tool_proficiencies))
        self.saving_throws_proficiencies = list(set(self.saving_throws_proficiencies) | set(dnd_class.saving_throws_proficiencies))
        self.skill_proficiencies = list(set(self.skill_proficiencies) | set(dnd_class.skill_proficiencies))
        self.equipment = merge_equipment(self.equipment, dnd_class.equipment)
        self.spellcasting_ability = dnd_class.spellcasting_ability
        self.languages = list(set(self.languages) | set(background.languages))
        self.wallet = Wallet()
        self.wallet.add_currency(background.starting_currency)
        self.conditions = []

        #for leveling up and limiting higher lvl features
        self.unlocked_features = []
        self.known_cantrips = []
        self.prepared_spells = {}   # {spell_level: [spell_name, ...]}
        self.spell_slots = {}       # {spell_level: num_slots}





    def set_ability_scores(self, ability_scores):
        self.ability_scores = ability_scores
        self.armor_class = 10 + self.ability_scores["dexterity"]
        self.max_hit_points = self.hit_dice.rounded_average*self.level + self.ability_scores["constitution"]



    def set_class(self, dnd_class):
        self.dnd_class = dnd_class
        self.hit_dice = dnd_class.hit_dice
        self.hit_dice_count = self.level
        if self.level == 1:
            self.max_hit_points = self.hit_dice.faces + self.ability_scores["constitution"]
        else:
            self.max_hit_points = self.hit_dice.rounded_average*self.level + self.ability_scores["constitution"]
        self.hit_points = self.max_hit_points
        self.hit_dice_count = self.level
        self.armor_proficiencies = list(set(self.armor_proficiencies) | set(dnd_class.armor_proficiencies))
        self.weapon_proficiencies = list(set(self.weapon_proficiencies) | set(dnd_class.weapon_proficiencies))
        self.tool_proficiencies = list(set(self.tool_proficiencies) | set(dnd_class.tool_proficiencies))
        self.saving_throws_proficiencies = list(set(self.saving_throws_proficiencies) | set(dnd_class.saving_throws_proficiencies))
        self.skill_proficiencies = list(set(self.skill_proficiencies) | set(dnd_class.skill_proficiencies))
        
        for item, amount in dnd_class.starting_equipment.items():
            self.equipment[item] = self.equipment.get(item, 0) + amount


    def set_race(self, race):
        self.race = race

    def set_background(self, background):
        self.background = background

    def set_alignment(self, alignment):
        self.alignment = alignment


    def move(self, direction, dt):
        speed = self.speed
        if (Condition.PETRIFIED in self.conditions
        or Condition.GRAPPLED in self.conditions
        or Condition.INCAPACITATED in self.conditions
        or Condition.PARALYZED in self.conditions
        or Condition.PRONE in self.conditions
        or Condition.STUNNED in self.conditions
        or Condition.UNCONSCIOUS in self.conditions):
            speed = 0

        if direction == "up":
            self.player_pos.y -= speed * dt
        elif direction == "down":
            self.player_pos.y += speed * dt
        elif direction == "left":
            self.player_pos.x -= speed * dt
        elif direction == "right":
            self.player_pos.x += speed * dt


    def update(self, screen, dt):
        #prevents spamming spells
        if self.cast_cooldown > 0:
            self.cast_cooldown -= dt
            if self.cast_cooldown < 0:
                self.cast_cooldown = 0

        self.draw(screen)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.player_pos, 20)
    

    def __str__(self):
        return f"Lvl:{self.level} {self.race} {self.dnd_class} {self.name}({self.hit_points}/{self.max_hit_points})"


def merge_equipment(dict1, dict2):
    result = dict1.copy()
    for item, amount in dict2.items():
        result[item] = result.get(item, 0) + amount
    return result