from GameState import *
from TextureManager import *

class MenuState(GameState):
    # State ID
    menuID = "MENU"
    
    def __init__(self, game) -> None:
        self.game = game

    def update(self):
        self.game.renderer.present()
        self.game.window.show()

    def render(self):
        self.game.renderer.clear()
        TextureManager().draw(self.game.renderer, "test", 0, 0, 128, 128, 1)

    def onEnter(self) -> bool:
        print("Entering menu state...")
        return True

    def onExit(self) -> bool:
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
