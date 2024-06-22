import pygame
from constants import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image, position, hitbox_x, hitbox_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y

    def update(self, dt):
        self.rect.x -= ASTEROID_MOVE_SPEED * dt