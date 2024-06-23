import pygame

from States.game_state import GameState
from Resources.Scripts.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_MOVE_SPEED
from Resources.Scripts.events import GAME_STARTED_EVENT, MAIN_MENU_ENTERED_EVENT, PLAYER_COLLIDED_EVENT


class GameOver(GameState):
    def __init__(self, screen):
        self.screen = screen

        self.bg_image = pygame.image.load('Resources/Images/background.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.i = 0
        self.score = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.event.post(pygame.event.Event(
                        GAME_STARTED_EVENT, {'message': 'Game started!'}))
                elif event.key == pygame.K_m:
                    pygame.event.post(pygame.event.Event(
                        MAIN_MENU_ENTERED_EVENT, {'message': 'Main menu entered.'}))
            elif event.type == PLAYER_COLLIDED_EVENT:
                self.score = int(float(event.message))

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
        font_mid = pygame.font.SysFont(None,70)
        font_small = pygame.font.SysFont(None, 36)

        self.text_surface1 = font_big.render(
            'GAME OVER!', True, (255, 255, 255))
        self.text_surface2 = font_mid.render(
            f'YOUR SCORE: {self.score}', True, (255, 255, 255))
        self.text_surface3 = font_small.render(
            'To try again press Enter', True, (255, 255, 255))
        self.text_surface4 = font_small.render(
            'To go to Main Menu press m', True, (255, 255, 255))

        self.text_rect1 = self.text_surface1.get_rect()
        self.text_rect2 = self.text_surface2.get_rect()
        self.text_rect3 = self.text_surface3.get_rect()
        self.text_rect4 = self.text_surface4.get_rect()

        self.screen.blit(self.text_surface1, ((
            SCREEN_WIDTH-self.text_rect1.width)/2, (SCREEN_HEIGHT-self.text_rect1.height)/2-self.text_rect2.height-150))
        self.screen.blit(self.text_surface2, ((
            SCREEN_WIDTH-self.text_rect2.width)/2, (SCREEN_HEIGHT-self.text_rect2.height)/2-self.text_rect2.height-50))
        self.screen.blit(self.text_surface3, ((
            SCREEN_WIDTH-self.text_rect3.width)/2, (SCREEN_HEIGHT-self.text_rect3.height)/2))
        self.screen.blit(self.text_surface4, ((
            SCREEN_WIDTH-self.text_rect4.width)/2, (SCREEN_HEIGHT-self.text_rect4.height)/2+self.text_rect2.height+20))
