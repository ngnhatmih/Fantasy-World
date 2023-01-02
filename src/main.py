import sdl2, sdl2.ext
from constant import *

class FantasyWorld:

    def __init__(self):

        sdl2.ext.init()

        self.window = sdl2.ext.Window("Title", size)
        self.renderer = sdl2.ext.renderer.Renderer(self.window, flags = sdl2.SDL_RENDERER_ACCELERATED)
        

    def run(self):

        self.window.show()
        self.isRunning = True
        while self.isRunning:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_Quit:
                    self.isRunning = False

            self.renderer.color = sdl2.ext.Color(*colors['white'], 0)
            self.renderer.clear()
            self.renderer.color = sdl2.ext.Color(*colors['violet'], 255)

            self.renderer.fill((100,100,100,100))

            self.renderer.present()

            self.window.refresh()

        self.renderer.destroy()
        self.window.close()
        sdl2.ext.quit()

if __name__ == "__main__":
    game = FantasyWorld()
    game.run()
