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
    
    mouseButtonStates = []

    def __init__(self):
        for i in range(3):
            self.mouseButtonStates.append(False)
        self.mPos = Vector2D([0,0]) # Mouse's Position

    #/Mouse/
    def getMouseButtonState(self, buttonNum : int)-> bool:
        return self.mouseButtonStates[buttonNum]
    
    def getMousePos(self)->Vector2D:
        return self.mPos
    
    def onMouseButtonDown(self, event: sdl2.SDL_Event):
        self.onMouseMove(event)
        print(self.getMousePos())
        match event.button.button:
            case sdl2.SDL_BUTTON_LEFT:
                self.mouseButtonStates[MouseButtons.LEFT.value] = True
            case sdl2.SDL_BUTTON_RIGHT:
                self.mouseButtonStates[MouseButtons.RIGHT.value] = True
            case sdl2.SDL_BUTTON_MIDDLE:
                self.mouseButtonStates[MouseButtons.MIDDLE.value] = True

    def onMouseButtonUp(self, event: sdl2.SDL_Event):
        match event.button.button:
            case sdl2.SDL_BUTTON_LEFT:
                self.mouseButtonStates[MouseButtons.LEFT.value] = False
            case sdl2.SDL_BUTTON_RIGHT:
                self.mouseButtonStates[MouseButtons.RIGHT.value] = False
            case sdl2.SDL_BUTTON_MIDDLE:
                self.mouseButtonStates[MouseButtons.MIDDLE.value] = False

    def onMouseMove(self, event: sdl2.SDL_Event):
        self.mPos.setX(event.motion.x)
        self.mPos.setY(event.motion.y)

    def reset(self):
        for i in range(3):
            self.mouseButtonStates.append(False)
        

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
                case sdl2.SDL_MOUSEBUTTONDOWN:
                    self.onMouseButtonDown(event)
                case sdl2.SDL_MOUSEBUTTONUP:
                    self.onMouseButtonUp(event)

        return isRunning