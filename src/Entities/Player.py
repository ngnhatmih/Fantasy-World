from creature import Creature

class Player(Creature):
    def __init__(self, name, sprite, description, species, level, exp, hit_points, strength, agility, defense, accuracy, critical_hit, critical_hit_chance, inventory):
        super().__init__(name, sprite, description, species, level, exp, hit_points, strength, agility, defense, accuracy, critical_hit, critical_hit_chance)
        self.inventory = inventory

import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
