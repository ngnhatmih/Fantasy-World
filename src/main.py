import sdl2, sdl2.ext
from constant import *

class FantasyWorld:

    def __init__(self, size):

        # Note myself in future checking whether each command (intialize, window creation, ...) suceed

        # Initialize SDL
        sdl2.ext.init()

        # Create the window and renderer
        self.window = sdl2.ext.Window("Fantasy World", size)
        self.renderer = sdl2.ext.renderer.Renderer(self.window, flags = sdl2.SDL_RENDERER_ACCELERATED)

        self.window.show()

        self.isRunning = True

    # Event handling function
    def handleEvents(self):

        for event in sdl2.ext.get_events():
            match event.type:
                case sdl2.SDL_Quit:
                    self.isRunning = False
                

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
    def clean(self):
         
        self.renderer.destroy()
        self.window.close()
        sdl2.ext.quit()

if __name__ == "__main__":

    # Initilize with a certain size
    game = FantasyWorld(size)

    # Game loop
    while game.isRunning:
        
        game.handleEvents()
        game.render()
        game.update()
    
    game.clean()