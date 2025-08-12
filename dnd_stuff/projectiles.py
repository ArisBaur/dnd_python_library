import pygame
import dnd_stuff.dice as dice
from math import sin, cos, radians

class projectile:
    def __init__(self, position, direction, ability_modifier):
        self.position = position
        self.direction = direction
        self.ability_modifier = ability_modifier
        self.speed = None

    def update(self, screen, dt):
        self.move(self.speed, dt)
        if self.is_off_screen(1280, 720):
            return False
        self.draw(screen)
        return True


    def move(self, speed, dt):
        rad = radians(self.direction)
        self.position.x += sin(rad) * 100 * speed * dt
        self.position.y += cos(rad) * 100 * speed * dt

    def is_off_screen(self, screen_width, screen_height):
        return (
            self.position.x < 0 or
            self.position.x > screen_width or
            self.position.y < 0 or
            self.position.y > screen_height
        )




class fireball(projectile):
    def __init__(self, position, direction, ability_score):
        super().__init__(position, direction, 0)
        self.damage = dice.d6() + ability_score
        self.speed = 30

    def draw(self, screen):
        print(f"Drawing fireball at {self.position} with damage {self.damage}")
        pygame.draw.circle(screen, "red", (int(self.position.x), int(self.position.y)), 20)    