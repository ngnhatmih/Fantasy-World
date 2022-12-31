from creature import Creature

class Player(Creature):
    def __init__(self, name, sprite, species, level, exp, hit_points, strength, agility, defense, accuracy, critical_hit, critical_hit_chance, inventory):
        super().__init__(name, sprite, species, level, exp, hit_points, strength, agility, defense, accuracy, critical_hit, critical_hit_chance)
        self.inventory = inventory
        