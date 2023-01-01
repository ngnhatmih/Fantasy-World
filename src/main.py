import pygame
from constant import *
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_ESCAPE, QUIT)
# added comment
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill(colors['white'])
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

pygame.init()

player = Player()

screen = pygame.display.set_mode(SIZE)

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
        
        elif event.type == QUIT:
            isRunning == False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill(colors['black'])

    screen.blit(player.surf, CENTER)

    
    pygame.display.flip()

pygame.quit()