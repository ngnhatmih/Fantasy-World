SIZE = HEIGHT, WIDTH = 320, 640
CENTER = HEIGHT/2, WIDTH/2

FPS = 60
DELAY = int(1000/FPS)

import enum

class MouseButtons(enum.Enum):
    LEFT = 0
    MIDDLE = 1
    RIGHT = 0
    
class Colors(enum.Enum): 
    RED = (255, 0, 0, 1.0)
    GREEN = (0, 255, 0, 1.0)
    BLUE = (0, 0, 255, 1.0)
    YELLOW = (255, 255, 0, 1.0)
    PURPLE = (255, 0, 255, 1.0)
    ORANGE = (255, 165, 0, 1.0)
    PINK = (255, 192, 203, 1.0)
    BLACK = (0, 0, 0, 1.0)
    WHITE = (255, 255, 255, 1.0)
    GRAY = (128, 128, 128, 1.0)
    BROWN = (165, 42, 42, 1.0)
    TAN = (210, 180, 140, 1.0)
