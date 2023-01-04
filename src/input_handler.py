import sdl2, sdl2.ext
import ctypes
from constant import *
from vector2D import *
class Singleton(type):
    
    _instances = {}
    def __call__(self, *args, **kwargs):

        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance

        return self._instances[self]

class InputHandler(metaclass = Singleton):

    #/Mouse/
    
    #/Keyboard/
    def onKeyDown(self, event: sdl2.SDL_Event):
        print("Key pressed:", sdl2.SDL_GetKeyName(event.key.keysym.sym))
    
    def onKeyUp(self, event: sdl2.SDL_Event):
        print("Key pressed:", sdl2.SDL_GetKeyName(event.key.keysym.sym))

    def isKeyDown(self, key : sdl2.SDL_Scancode)->bool:
        print(self.keystates != 0)
        if self.keystates != 0:
            if self.keystates[key] == 1:
                return True
            else: return False
        else: return False
    
    def update(self)->bool:

        self.keystates : sdl2.Uint8 = sdl2.SDL_GetKeyboardState(ctypes.c_long(0))
        isRunning = True

        for event in sdl2.ext.get_events():
            match event.type:
                case sdl2.SDL_QUIT:
                    isRunning = False
                case sdl2.SDL_KEYDOWN:
                    self.onKeyDown(event)
                case sdl2.SDL_KEYUP:
                    self.onKeyUp(event)

        return isRunning