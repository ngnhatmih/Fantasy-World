from GameState import *
from GameStateMachine import *
from TextureManager import *
from Game import *

class State(GameState):
    stateID = "STATE"

    def update(self):
        pass

    def render(self):
        pass

    def onEnter(self) -> bool:
        return True

    def onExit(self) -> bool:
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