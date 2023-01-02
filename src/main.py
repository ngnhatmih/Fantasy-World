from game import *

if __name__ == "__main__":
    game = FantasyWorld()

    while game.isRunning:
        game.handleEvents()
        game.render()
        game.update()
    
    game.clean()