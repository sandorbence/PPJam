import pygame
import random

from States.game_state import GameState
from player import Player
from asteroid_factory import AsteroidFactory
from constants import *


class Playing(GameState):
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pygame.image.load('Resources/Images/background.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        player_sprite = pygame.image.load(
            'Resources/Sprites/Player/playerShip1_blue.png')
        player_pos = pygame.Vector2(
            screen.get_width() / 2, screen.get_height() / 2)
        player_sprite = pygame.transform.rotate(player_sprite, 270)

        player = Player(player_sprite, player_pos)

        self.player_sprite_group = pygame.sprite.Group()
        self.player_sprite_group.add(player)

        self.asteroid_sprite_group = pygame.sprite.Group()

        self.asteroid_counter = 0
        self.next_asteroid = random.randrange(
            ASTEROID_MIN_SPAWN_TIME, ASTEROID_MAX_SPAWN_TIME) / 100

        self.i = 0

    def handle_events(self, events):
        return super().handle_events()

    def update(self, dt):
        if self.i <= -SCREEN_WIDTH:
            self.i = 0
        self.i -= BACKGROUND_MOVE_SPEED

        self.player_sprite_group.update(dt)

        self.asteroid_counter += dt

        if self.asteroid_counter >= self.next_asteroid:
            asteroid = AsteroidFactory.create()
            self.asteroid_sprite_group.add(asteroid)

            self.next_asteroid = random.randrange(
                ASTEROID_MIN_SPAWN_TIME, ASTEROID_MAX_SPAWN_TIME) / 100
            self.asteroid_counter = 0

        self.asteroid_sprite_group.update(dt)

    def render(self):
        self.screen.blit(self.bg_image, (self.i, 0))
        self.screen.blit(self.bg_image, (SCREEN_WIDTH+self.i, 0))
        self.player_sprite_group.draw(self.screen)
        self.asteroid_sprite_group.draw(self.screen)
