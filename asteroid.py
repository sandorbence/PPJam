import pygame
from constants import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.position = position

    def update(self, dt):
        self.rect.x -= ASTEROID_MOVE_SPEED * dt