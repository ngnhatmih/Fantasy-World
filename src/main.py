import pygame
from constant import *
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_ESCAPE, QUIT)

pygame.init()
screen = pygame.display.set_mode(size)

SURF_SIZE = SURF_WIDTH, SURF_HEIGHT= 50, 50

isRunning = True

while(isRunning):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
    
    screen.fill(colors['white'])

    surf = pygame.Surface(SURF_SIZE)
    surf.fill(colors['black'])

    rect = surf.get_rect()

    screen.blit(surf, ((WIDTH - SURF_WIDTH)/2, (HEIGHT - SURF_HEIGHT)/2))
    pygame.display.flip()

pygame.quit()

