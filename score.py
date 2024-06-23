import pygame
from constants import SCORE_MULTIPLIER


class Score():
    def __init__(self, screen):
        self.screen = screen
        self.value = 0

    def update(self, dt):
        self.value += dt * SCORE_MULTIPLIER

    def render(self):
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(
            f'SCORE: {int(self.value)}', True, (255, 255, 255))
        self.screen.blit(text_surface, (20, 20))
