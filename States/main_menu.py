import pygame

from States.game_state import GameState
from constants import *
from events import GAME_START_EVENT


class MainMenu(GameState):
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pygame.image.load('Resources/Images/background.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.i = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.event.post(pygame.event.Event(
                    GAME_START_EVENT, {'message': 'Game started!'}))

    def update(self, dt):

        if self.i <= -SCREEN_WIDTH:
            self.i = 0
        self.i -= BACKGROUND_MOVE_SPEED

    def render(self):
        self.screen.blit(self.bg_image, (self.i, 0))
        self.screen.blit(self.bg_image, (SCREEN_WIDTH+self.i, 0))
