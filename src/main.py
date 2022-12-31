import pygame
from constant import *

pygame.init()
screen = pygame.display.set_mode(size, 0, 32)

isRunning = True
i = 0
while(isRunning):
    i+=1
    if i == 255:
        i = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning == False
    
    screen.fill((i,0,255))

    pygame.display.flip()

pygame.quit()