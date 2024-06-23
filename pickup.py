import pygame
from constants import *


class Pickup(pygame.sprite.Sprite):
    def __init__(self, position, pace):
        super().__init__()
        self.image = pygame.image.load(
            'Resources/Images/pickup.png')
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width()/4, self.image.get_height()/4))
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.hitbox_x = self.image.get_width()
        self.hitbox_y = self.image.get_height()
        self.pace = pace

    def update(self, dt):
        position_change = PICKUP_MOVE_SPEED * dt*self.pace
        self.rect.x -= position_change
        self.position.x -= position_change
