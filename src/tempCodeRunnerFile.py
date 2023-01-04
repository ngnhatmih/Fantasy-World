
        game.handleEvents()
        game.render()
        game.update()
        frameTime = sdl2.SDL_GetTicks() - frameStart

        
        if frameTime < DELAY_TIME:
            delay = DELAY_TIME-frameTime
        else:
            delay = frameTime

        sdl2.SDL_Delay(delay)