import pygame
from dnd_stuff.conditions import Condition
from math import sin, cos, radians, floor

from dnd_stuff.wallet import Wallet



class player:
    def __init__(self, name, level, background):
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
        self.dnd_class = None
        self.level = min(level, 20)
        self.background = background
        self.race = None
        self.alignment = None
        self.ability_scores = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }
        self.proficiency_bonus = None
        self.armor_class = None
        self.initiative = None
        self.speed = None
        self.max_hit_points = None
        self.hit_dice = None
        self.hit_points = None
        self.hit_dice_count = level
        self.death_saves = {"success": 0, "failure": 0}
        self.armor_proficiencies = []
        self.weapon_proficiencies = []
        self.tool_proficiencies = []
        self.saving_throws_proficiencies = []
        self.skill_proficiencies = []
        self.languages = []
        self.equipment = {} # {item_name: item_quantity}
        self.wallet = Wallet()
        self.conditions = []

        #for leveling up and limiting higher lvl abilities
        self.unlocked_abilities = []
        self.known_cantrips = []
        self.prepared_spells = {}   # {spell_level: [spell_name, ...]}
        self.spell_slots = {}       # {spell_level: num_slots}

        

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
        return f"Lvl:{self.level} {self.dnd_class} {self.name}({self.hit_points}/{self.max_hit_points})"
