import sdl2, sdl2.ext
from constant import *
from input_handler import *
from texture_manager import *

path = b"path/to/texture.bmp"

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

        TextureManager().load(path, "test", self.getRenderer())

    # Event handling function
    def handleEvents(self):
        self.isRunning = InputHandler().update()
        
                        
    def getRenderer(self) -> sdl2.ext.renderer.Renderer:
        return self.renderer

    # Render function
    def render(self):
        self.renderer.clear()
        TextureManager().draw("test", 100, 100, 128, 128, 1, 0, self.getRenderer(), sdl2.SDL_FLIP_NONE)
        TextureManager().drawFrame("test", 300, 300, 128, 128, 1, 0, 0, 0, self.getRenderer())

    def update(self):
        self.renderer.present()
        self.window.refresh()

    # Clean up
    def clean(self)->bool:
        TextureManager().cleanFromTextureMap("test")
        self.renderer.destroy()
        self.window.close()
        sdl2.ext.quit()

        return True
