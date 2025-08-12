import pygame
import player



class Wizard(player):
    def __init__(self, label, level, background):
        super().__init__(name, level, background)
        # pygame stuff
        self.class_sprite_path = "assets/sprites/wizard.png"
        self.race_sprite_path = "assets/sprites/human.png"
        self.cast_cooldown = 0
        self.spell_cooldown_time = 1.5

        #dnd stuff
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
        self.equipment = {}
        self.conditions = []

        #for leveling up and limiting higher lvl abilities
        self.unlocked_abilities = []
        self.known_cantrips = []
        self.prepared_spells = {}   # {spell_level: [spell_name, ...]}
        self.spell_slots = {}       # {spell_level: num_slots}




    def draw(self, screen):
        if (self.sprite_path == None):
            pygame.draw.circle(screen, "white", self.player_pos, 20)
        else:
            sprites = [
                pygame.image.load(f"{self.sprite_path}_down.png"),
                pygame.image.load(f"{self.sprite_path}_right.png"),
                pygame.image.load(f"{self.sprite_path}_up.png"),
                pygame.image.load(f"{self.sprite_path}_left.png")]
            
            sprite_index = int((self.direction + 45) // 90) % 4
            self.sprite = sprites[sprite_index]
            self.sprite = pygame.transform.scale(self.sprite, (100 * self.sprite.get_height()/self.sprite.get_width(), 100))
            screen.blit(self.sprite, (self.player_pos.x - self.sprite.get_width() / 2, self.player_pos.y - self.sprite.get_height() / 2))
            
