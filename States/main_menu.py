import pygame

from States.game_state import GameState
from constants import *
from events import GAME_STARTED_EVENT


class MainMenu(GameState):
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pygame.image.load('Resources/Images/background.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.i = 0
        self.text_to_show = 'main_menu'

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RETURN:
                        pygame.event.post(pygame.event.Event(
                            GAME_STARTED_EVENT, {'message': 'Game started!'}))
                    case pygame.K_x:
                        self.text_to_show = 'controls'
                    case pygame.K_c:
                        self.text_to_show = 'credits'
                    case pygame.K_ESCAPE:
                        self.text_to_show = 'main_menu'

    def update(self, dt):
        if self.i <= -SCREEN_WIDTH:
            self.i = 0
        self.i -= BACKGROUND_MOVE_SPEED

    def render(self):
        self.screen.blit(self.bg_image, (self.i, 0))
        self.screen.blit(self.bg_image, (SCREEN_WIDTH+self.i, 0))

        self.render_text()

    def render_text(self):
        font_big = pygame.font.SysFont(None, 120)
        font_small = pygame.font.SysFont(None, 45)
        font_credits = pygame.font.SysFont(None, 32)

        match self.text_to_show:
            case 'main_menu':
                text_surface1 = font_big.render(
                    'BLASTEROID', True, (255, 255, 255))
                text_surface2 = font_small.render(
                    'Start Game: Enter', True, (255, 255, 255))
                text_surface3 = font_small.render(
                    'Controls: x', True, (255, 255, 255))
                text_surface4 = font_small.render(
                    'Credits: c', True, (255, 255, 255))

                text_rect1 = text_surface1.get_rect()
                text_rect2 = text_surface2.get_rect()
                text_rect3 = text_surface3.get_rect()
                text_rect4 = text_surface4.get_rect()

                self.screen.blit(text_surface1, ((
                    SCREEN_WIDTH-text_rect1.width)/2, (SCREEN_HEIGHT-text_rect1.height)/2-text_rect2.height-150))
                self.screen.blit(text_surface2, ((
                    SCREEN_WIDTH-text_rect2.width)/2, (SCREEN_HEIGHT-text_rect2.height)/2))
                self.screen.blit(text_surface3, ((
                    SCREEN_WIDTH-text_rect3.width)/2, (SCREEN_HEIGHT-text_rect3.height)/2+70))
                self.screen.blit(text_surface4, ((
                    SCREEN_WIDTH-text_rect4.width)/2, (SCREEN_HEIGHT-text_rect4.height)/2+140))
            case 'controls':
                text_surface1 = font_small.render(
                    'Movement: w, a, s, d', True, (255, 255, 255))
                text_surface2 = font_small.render(
                    'Shooting: Space', True, (255, 255, 255))
                text_surface3 = font_small.render(
                    'Press Esc to go back to Main Menu', True, (255, 255, 255))

                text_rect1 = text_surface1.get_rect()
                text_rect2 = text_surface2.get_rect()
                text_rect3 = text_surface3.get_rect()

                self.screen.blit(text_surface1, ((
                    SCREEN_WIDTH-text_rect1.width)/2, (SCREEN_HEIGHT-text_rect1.height)/2-text_rect2.height-50))
                self.screen.blit(text_surface2, ((
                    SCREEN_WIDTH-text_rect2.width)/2, (SCREEN_HEIGHT-text_rect2.height)/2))
                self.screen.blit(text_surface3, ((
                    SCREEN_WIDTH-text_rect3.width)/2, (SCREEN_HEIGHT-text_rect3.height)/2+text_rect2.height+50))
            case 'credits':
                text_surface1 = font_credits.render(
                    'Created by: Sándor Bence & Bakon Bence', True, (255, 255, 255))
                text_surface2 = font_credits.render(
                    'Background music: Pix - https://www.youtube.com/watch?v=G2nmOULeOBQ&list=PPSV&ab_channel=Pix', True, (255, 255, 255))
                text_surface3 = font_credits.render(
                    'Player image: Kenney.nl', True, (255, 255, 255))
                text_surface4 = font_credits.render(
                    'Powerup and rocket image: https://craftpix.net/', True, (255, 255, 255))
                text_surface5 = font_credits.render(
                    'https://github.com/sandorbence/PPJam', True, (255, 255, 255))
                text_surface6 = font_small.render(
                    'Press Esc to go back to Main Menu', True, (255, 255, 255))

                text_rect1 = text_surface1.get_rect()
                text_rect2 = text_surface2.get_rect()
                text_rect3 = text_surface3.get_rect()
                text_rect4 = text_surface4.get_rect()
                text_rect5 = text_surface5.get_rect()
                text_rect6 = text_surface6.get_rect()

                self.screen.blit(text_surface1, ((
                    SCREEN_WIDTH-text_rect1.width)/2, (SCREEN_HEIGHT-text_rect1.height)/2-150))
                self.screen.blit(text_surface2, ((
                    SCREEN_WIDTH-text_rect2.width)/2, (SCREEN_HEIGHT-text_rect1.height)/2-100))
                self.screen.blit(text_surface3, ((
                    SCREEN_WIDTH-text_rect3.width)/2, (SCREEN_HEIGHT-text_rect1.height)/2-50))
                self.screen.blit(text_surface4, ((
                    SCREEN_WIDTH-text_rect4.width)/2, (SCREEN_HEIGHT-text_rect1.height)/2))
                self.screen.blit(text_surface5, ((
                    SCREEN_WIDTH-text_rect5.width)/2, (SCREEN_HEIGHT-text_rect1.height)/2+50))
                self.screen.blit(text_surface6, ((
                    SCREEN_WIDTH-text_rect6.width)/2, (SCREEN_HEIGHT-text_rect6.height)/2+250))
