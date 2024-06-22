import pygame

from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.position = position

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_s]:
            self.rect.y += PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_MOVE_SPEED * dt
