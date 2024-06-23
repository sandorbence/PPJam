import pygame
from constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image, position, hitbox_x, hitbox_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.hasRocket = False
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y

    def update(self, dt):
        keys = pygame.key.get_pressed()
        position_change = PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= position_change
            self.position.y -= position_change
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += position_change
            self.position.y += position_change
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= position_change
            self.position.x -= position_change
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += position_change
            self.position.x += position_change
