import pygame

from constants import ASTEROID_MOVE_SPEED


class Rocket(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        sprite = pygame.image.load('Resources/Props/Missile_01.png')
        self.image = pygame.transform.rotate(sprite, 90)
        self.position = position

    def update(self, dt):
        position_change = ASTEROID_MOVE_SPEED * dt
        self.rect.x += position_change
        self.position.x -= position_change