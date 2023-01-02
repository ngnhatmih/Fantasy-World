import sdl2, sdl2.ext
from constant import *
from inputHandler import *

class FantasyWorld:

    def __init__(self):
        # Note myself in future checking whether each command (intialize, window creation, ...) suceed

        # Initialize SDL
        sdl2.ext.init()

        # Create the window and renderer
        self.window = sdl2.ext.Window("Fantasy World", size, flags = sdl2.SDL_WINDOW_RESIZABLE)
        self.renderer = sdl2.ext.renderer.Renderer(self.window, flags = sdl2.SDL_RENDERER_ACCELERATED)

        self.window.show()

        self.isRunning = True

    # Event handling function
    def handleEvents(self):
        self.isRunning = inputHandler().update()
                        
                             
    # Render function
    def render(self):
        self.renderer.color = sdl2.ext.Color(*colors['white'], 0)
        self.renderer.clear()
        self.renderer.color = sdl2.ext.Color(*colors['violet'], 255)

        self.renderer.fill((100,100,100,100))

    def update(self):
        self.renderer.present()
        self.window.refresh()

    # Clean up
    def clean(self)->bool:
        self.renderer.destroy()
        self.window.close()
        sdl2.ext.quit()

        return True
