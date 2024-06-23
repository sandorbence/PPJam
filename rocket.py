import pygame

from constants import ASTEROID_MOVE_SPEED


class Rocket(pygame.sprite.Sprite):
    def __init__(self, position, pace):
        super().__init__()
        sprite = pygame.image.load('Resources/Images/rocket.png')
        self.image = pygame.transform.rotate(sprite, 270)
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() / 4, self.image.get_height() / 4))
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.hitbox_x = self.rect.width
        self.hitbox_y = self.rect.height
        self.pace = pace

    def update(self, dt):
        position_change = ASTEROID_MOVE_SPEED * dt * self.pace
        self.rect.x += position_change
        self.position.x += position_change
