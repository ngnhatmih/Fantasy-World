import sdl2, sdl2.ext
import ctypes

class Singleton(type):

    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance

        return self._instances[self]

class InputHandler(metaclass = Singleton):

    def __init__(self):
        pass

    def onKeyDown(self, event : sdl2.SDL_Event):
        print("Key pressed: ", sdl2.SDL_GetKeyName(event.key.keysym.sym))
    
    def onKeyUp(self, event : sdl2.SDL_Event):
        print("Key pressed: ", sdl2.SDL_GetKeyName(event.key.keysym.sym))

    def update(self)->bool:
        isRunning = True
        self.keystates : sdl2.Uint8 = sdl2.SDL_GetKeyboardState(ctypes.c_long(0))

        for event in sdl2.ext.get_events():
            match event.type:
                case sdl2.SDL_QUIT:
                    isRunning = False
                case sdl2.SDL_KEYDOWN:
                    self.onKeyDown(event)
                case sdl2.SDL_KEYUP:
                    self.onKeyUp(event)

        return isRunning
