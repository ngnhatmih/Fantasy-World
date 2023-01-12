import sdl2, sdl2.ext
import InputHandler
from TextureManager import *
from Constant import *

class Singleton(type):
    # This variable is used to store all instances initialized
    instances = {}
    
    # __call__ makes the class itself become a function whenever it is called
    def __call__(self, *args, **kwds):
        # Check whether the instance is in instances
        if self not in self.instances:
            instance = super().__call__(*args, **kwds)
            self.instances[self] = instance
        return self.instances[self]  

class Game(metaclass = Singleton):
    version = 0.0

    def __init__(self):
        # Initialize SDL and its subsystems
        # Subsystems (default): video=True, audio=False, timer=False, joystick=False,
        # controller=False, haptic=False, sensor=False, events=True
        sdl2.ext.init()

        # Window Creation
        self.window = sdl2.ext.Window(f"Fantasy-World {self.version}", SIZE)

        # Renderer Creation
        self.renderer = sdl2.ext.renderer.Renderer(self.window, flags = sdl2.SDL_RENDERER_ACCELERATED)

        # Show the windows
        self.window.show() 

        # Is the game running?
        self.isRunning = True

        # Load the textures
        TextureManager().load("assets/textures/test.png", "test", self.renderer)
        self.currentFrame = 0

        
    # Event Handling
    def eventHandle(self):
        self.isRunning = InputHandler.InputHandler().update()

    def render(self):
        self.renderer.clear()
        TextureManager().drawFrame(self.renderer, "test", 0, 0, 64, 64, 1.0, self.currentFrame % 5, int(self.currentFrame/4))
        self.currentFrame += 1
        if self.currentFrame == 12:
            self.currentFrame = 0


    def update(self):
        self.renderer.present()
        self.window.refresh()
    
    # Clean up
    def clean(self):
        self.window.close()
        self.renderer.destroy()
        sdl2.ext.quit()