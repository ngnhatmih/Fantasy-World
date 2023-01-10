import sdl2, sdl2.ext
import InputHandler
from Constant import *

class Game:
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

        
    # Event Handling
    def eventHandle(self):
        self.isRunning = InputHandler.InputHandler().update()

    def render(self):
        pass

    def update(self):
        pass
    
    # Clean up
    def clean(self):
        self.window.close()
        self.renderer.destroy()
        sdl2.ext.quit()