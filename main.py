import pygame
import logging
import random

from collision_handler import CollisionHandler
from constants import *
from player import Player
from asteroid_factory import AsteroidFactory

# pygame setup
pygame.init()

logging.basicConfig(level=logging.DEBUG)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
i = 0

bg_image = pygame.image.load('Resources/Images/background.png')
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

player_sprite = pygame.image.load(
    'Resources/Sprites/Player/playerShip1_blue.png')
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_sprite = pygame.transform.rotate(player_sprite, 270)

player = Player(player_sprite, player_pos)

player_sprite_group = pygame.sprite.Group()
player_sprite_group.add(player)

asteroid_sprite_group = pygame.sprite.Group()
asteroid_group = []

asteroid_counter = 0
next_asteroid = random.randrange(
    ASTEROID_MIN_SPAWN_TIME, ASTEROID_MAX_SPAWN_TIME) / 100

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(bg_image, (i, 0))
    screen.blit(bg_image, (SCREEN_WIDTH+i, 0))
    if i <= -SCREEN_WIDTH:
        i = 0
    i -= BACKGROUND_MOVE_SPEED

    player.update(dt)
    player_sprite_group.draw(screen)

    asteroid_counter += dt

    if asteroid_counter >= next_asteroid and len(asteroid_group) < 1:
        asteroid = AsteroidFactory.create()
        asteroid_sprite_group.add(asteroid)
        asteroid_group.append(asteroid)
        
        next_asteroid = random.randrange(
        ASTEROID_MIN_SPAWN_TIME, ASTEROID_MAX_SPAWN_TIME) / 100
        asteroid_counter = 0

    CollisionHandler.checkPlayer(player, asteroid_group)

    asteroid_sprite_group.update(dt)
    asteroid_sprite_group.draw(screen)

    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
