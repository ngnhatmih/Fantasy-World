from enum import Enum

############################################

size = WIDTH, HEIGHT = 800, 600
CENTER = WIDTH/2, HEIGHT/2
FPS = 60
DELAY_TIME = 20

class Colors(Enum):
    RED = (255,0,0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    INDIGO = (75, 0, 130)
    VIOLET = (238, 130, 238)
    BROWN = (165, 42, 42)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

###########################################