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
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_MOVE_SPEED * dt
