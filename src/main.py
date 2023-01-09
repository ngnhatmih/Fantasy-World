import sys
from game import *

def main():
    # Initialize
    game = Game()

    # Game Loop
    while(game.isRunning):
        game.eventHandle()
        game.update()
        game.render()

    game.clean()
   
if __name__ == "__main__":
    sys.exit(main())