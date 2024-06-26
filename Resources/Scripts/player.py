import pygame
from Resources.Scripts.constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(
            'Resources/Images/player.png')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.hasRocket = False
        self.hitbox_x = self.rect.width
        self.hitbox_y = self.rect.height-20

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