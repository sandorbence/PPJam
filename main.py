import pygame

from constants import *
from player import Player

# pygame setup
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
i = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

bg_image = pygame.image.load('Resources/Images/background.png')
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

player_sprite = pygame.image.load(
    'Resources/Sprites/Player/playerShip1_blue.png')
player_sprite = pygame.transform.rotate(player_sprite, 270)
player = Player(player_sprite, player_pos)

player_sprite_group = pygame.sprite.Group()
player_sprite_group.add(player)

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

    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
