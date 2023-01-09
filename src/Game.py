import sdl2, sdl2.ext
from Constant import *

class Game:
    version = 0.0

    def __init__(self):
        # Initialize
        sdl2.ext.init()
        
        # Window Creation
        self.window = sdl2.ext.Window(f"Fantasy-World {self.version}", SIZE)

        # Renderer Creation
        self.renderer = sdl2.ext.renderer.Renderer(self.window, flags = sdl2.SDL_RENDERER_ACCELERATED)

        # Shows the windows
        self.window.show() 

        # Is the game running?
        self.isRunning = True

        

    def eventHandle(self):
        # Event Handling
        for event in sdl2.ext.get_events():
            match event.type:
                case sdl2.SDL_QUIT:
                    self.isRunning = False

    def render(self):
        pass

    def update(self):
        pass
    
    # Clean up
    def clean(self):
        self.window.close()
        self.renderer.destroy()
        sdl2.ext.quit()