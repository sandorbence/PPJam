class GameState():
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass

class MainMenu(GameState):
    def __init__(self):
        super().__init__()
        
    def update(self):
        return super().update()
        
    def render(self):
        return super().render()

class Playing(GameState):
    def __init__(self):
        super().__init__()
        
    def update(self):
        return super().update()
        
    def render(self):
        return super().render()

class GameOver(GameState):
    def __init__(self):
        super().__init__()
        
    def update(self):
        return super().update()
        
    def render(self):
        return super().render()