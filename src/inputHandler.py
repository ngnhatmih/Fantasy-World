import sdl2, sdl2.ext

class SingletonMeta(type):

    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance

        return self._instances[self]

class inputHandler(metaclass = SingletonMeta):
    def __init__(self):
        self.keystates : sdl2.Uint8 = None

    def isKeyDown(self, key: sdl2.SDL_Scancode)->bool:
        if self.keystates != 0:
            if self.keystates[key] == 1:
                return True
            else: return False
        else: return False

    def onKeyDown(self, event:sdl2.SDL_Event):
        print("Key Pressed: ", sdl2.SDL_GetKeyName(event.key.keysym.sym))

    def onKeyUp(self, event:sdl2.SDL_Event):
        print("Key Released: ", sdl2.SDL_GetKeyName(event.key.keysym.sym))

    def update(self):
        self.keystates : sdl2.Uint8 = sdl2.SDL_GetKeyboardState(0)

        for event in sdl2.ext.get_events():
            match event.type:
                case sdl2.SDL_KEYDOWN:
                    self.onKeyDown(event)
                case sdl2.SDL_KEYUP:
                    self.onKeyUp(event)
