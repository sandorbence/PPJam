import pygame
from constants import *


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image, position, hitbox_x, hitbox_y, pace):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.pace = pace

    def update(self, dt):
        position_change = ASTEROID_MOVE_SPEED * dt * self.pace
        self.rect.x -= position_change
        self.position.x -= position_change
