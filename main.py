import pygame
import logging

from States.state_manager import StateManager
from constants import *

# pygame setup
pygame.init()

logging.basicConfig(level=logging.DEBUG)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
state_manager = StateManager(screen)

while running:
    
    events = pygame.event.get()
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    state_manager.handle_events(events)
    state_manager.update(dt)
    state_manager.render()

    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
