import pygame
from constant import *
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_ESCAPE, QUIT)

pygame.init()
screen = pygame.display.set_mode(size)

isRunning = True
i = 0
while(isRunning):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning == False
        
    
    screen.fill((i,0,255))

    pygame.display.update()

pygame.quit()