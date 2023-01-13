from abc import ABC, abstractmethod
import sdl2

# An abstract class - a class cannot be instantiated
class GameState(ABC): # Declare abtract class
    # This decorator indicates this method has no implementation but can be overridden by any concrete subclass
    # In C/C++ this is a virtual function which should be overridden in subclass of the abstract class
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onEnter(self)->bool:
        pass

    @abstractmethod
    def onExit(self)->bool:
        pass

    @abstractmethod
    def onKeyDown(self, event: sdl2.SDL_Event):
        pass

    @abstractmethod
    def onKeyUp(self, event: sdl2.SDL_Event):
        pass

    @abstractmethod
    def onMouseButtonDown(self, event: sdl2.SDL_Event):
        pass

    @abstractmethod
    def onMouseButtonUp(self, event: sdl2.SDL_Event):
        pass

    @abstractmethod
    def onMouseMove(self, event: sdl2.SDL_Event):
        pass

    @abstractmethod
    @property
    def getStateID(self)->str:
        pass

