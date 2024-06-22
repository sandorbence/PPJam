from States.main_menu import MainMenu
from States.playing import Playing
from States.game_over import GameOver
from events import GAME_START_EVENT


class StateManager:
    def __init__(self, screen):
        self.states = {
            'main_menu': MainMenu(screen),
            'playing': Playing(screen),
            'game_over': GameOver(screen)
        }
        self.current_state = self.states['main_menu']

    def change_state(self, new_state):
        self.current_state = self.states[new_state]

    def handle_events(self, events):
        for event in events:
            if event.type == GAME_START_EVENT:
                self.change_state('playing')
        self.current_state.handle_events(events)

    def update(self, dt):
        self.current_state.update(dt)

    def render(self):
        self.current_state.render()
