from game_states import MainMenu, Playing, GameOver


class StateManager:
    def __init__(self):
        self.states = {
            'main_menu': MainMenu,
            'playing': Playing,
            'game_over': GameOver
        }
        self.current_state = self.states['main_menu']

    def change_state(self, new_state):
        self.current_state = self.states[new_state]

    def update(self):
        self.current_state.update()

    def render(self):
        self.current_state.render()
