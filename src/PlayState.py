from GameState import *
from TextureManager import *
from InputHandler import *

class PlayState(GameState):
    # State ID
    playID = "PLAY"

    # Pass game instance to avoid circular import
    def __init__(self, game) -> None:
        self.game = game
        self.gameObjects:GameObject = {}

    # Update all objects in play states
    def update(self):
        for value in self.gameObjects.values():
            value.update()
            
        self.game.renderer.present()
        self.game.window.show()

    # Draw objects
    def render(self):
        self.game.renderer.clear()
        self.game.getRenderer().color = sdl2.ext.Color(*Colors.GRAY.value)

        for value in self.gameObjects.values():
            value.draw()

    # Trigger this event when joinin this play state
    def onEnter(self) -> bool:
        print("Entering play state...")
        return True

    # Trigger this event when leavin this play state
    def onExit(self) -> bool:
        for value in self.gameObjects.values():
            value.clean()

        print("Exiting play state...")
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
        return self.playID
