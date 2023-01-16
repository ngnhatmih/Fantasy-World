from GameState import *
from TextureManager import *

class MenuState(GameState):
    # State ID
    menuID = "MENU"
    
    def __init__(self, game) -> None:
        self.game = game

    def update(self):
        for key, value in self.gameObjects.items():
            if key == list(self.gameObjects.keys())[-1]:
                break
            value.update()
            
        self.game.renderer.present()
        self.game.window.show()

    def render(self):
        self.game.renderer.clear()
        TextureManager().draw(self.game.renderer, "test", 0, 0, 128, 128, 1)
        
        for key, value in self.gameObjects.items():
            if key == list(self.gameObjects.keys())[-1]: 
                break
            value.draw()

    def onEnter(self) -> bool:
        self.gameObjects["penguin01"] = GameObject("test", 100, 100, 128, 128, 1.0, 1, self.game)
        self.gameObjects["penguin02"] = GameObject("test", 300, 300, 128, 128, 1.0, 1, self.game)
        print("Entering menu state...")
        return True

    def onExit(self) -> bool:
        for key, value in self.gameObjects.items():
            if key == list(self.gameObjects.keys())[-1]:
                break
            value.clean()

        print("Exiting menu state...")
        return True
    
    def onKeyDown(self, event: sdl2.SDL_Event):
        pass

    def onKeyUp(self, event: sdl2.SDL_Event):
        pass

    def onMouseButtonDown(self, event: sdl2.SDL_Event):
        pass

    def onMouseButtonUp(self, event: sdl2.SDL_Event):
        pass

    def onMouseMove(self, event: sdl2.SDL_Event):
        pass

    def getStateID(self) -> str:
        return self.menuID
