from States.game_state import MainMenu, Playing, GameOver


class StateManager:
    def __init__(self, screen):
        self.states = {
            'main_menu': MainMenu(screen),
            'playing': Playing(screen),
            'game_over': GameOver(screen)
        }
        self.current_state = self.states['playing']

    def change_state(self, new_state):
        self.current_state = self.states[new_state]

    def update(self, dt):
        self.current_state.update(dt)

    def render(self):
        self.current_state.render()
