import asyncio
import pygame

from States.state_manager import StateManager
from Resources.Scripts.constants import *

# pygame setup
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('Resources/Sounds/background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

state_manager = StateManager(screen)

async def main():

    running = True
    dt = 0
    
    while running:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        state_manager.handle_events(events)
        state_manager.update(dt)
        state_manager.render()

        pygame.display.update()

        dt = clock.tick(60) / 1000
        await asyncio.sleep(0)

asyncio.run(main())
