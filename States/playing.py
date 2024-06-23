import pygame
import random

from States.game_state import GameState
from player import Player
from asteroid_factory import AsteroidFactory
from constants import *
from collision_handler import CollisionHandler


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

        self.player = Player(player_sprite, player_pos)

        self.player_sprite_group = pygame.sprite.Group()
        self.player_sprite_group.add(self.player)

        self.asteroid_sprite_group = pygame.sprite.Group()
        self.asteroid_group = []
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
            self.asteroid_group.append(asteroid)
            self.next_asteroid = random.randrange(
                ASTEROID_MIN_SPAWN_TIME, ASTEROID_MAX_SPAWN_TIME) / 100
            self.asteroid_counter = 0

        self.asteroid_sprite_group.update(dt)

        CollisionHandler.checkPlayer(self.player, self.asteroid_group)
        
        for asteroid in self.asteroid_group:
            if asteroid.rect.right < 0:
                self.asteroid_group.remove(asteroid)
                self.asteroid_sprite_group.remove(asteroid)

    def render(self):
        self.screen.blit(self.bg_image, (self.i, 0))
        self.screen.blit(self.bg_image, (SCREEN_WIDTH+self.i, 0))
        self.player_sprite_group.draw(self.screen)
        self.asteroid_sprite_group.draw(self.screen)
