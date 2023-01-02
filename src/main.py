from game import *

if __name__ == "__main__":
    game = FantasyWorld()

    while game.isRunning:

        frameStart = sdl2.SDL_GetTicks()
        game.handleEvents()
        game.render()
        game.update()
        frameTime = sdl2.SDL_GetTicks() - frameStart

         #ye
        if frameTime < DELAY_TIME:
            delay = DELAY_TIME-frameTime
        else:
            delay = frameTime

        sdl2.SDL_Delay(delay)
        print("Delay: ", delay)
        
    game.clean()