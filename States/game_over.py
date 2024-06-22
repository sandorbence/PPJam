from States.game_state import GameState


class GameOver(GameState):
    def __init__(self, screen):
        self.screen = screen

    def handle_events(self, events):
        return super().handle_events()

    def update(self, dt):
        return super().update()

    def render(self):
        return super().render()
