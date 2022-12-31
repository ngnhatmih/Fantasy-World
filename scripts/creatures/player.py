from creature import Creature

class Player(Creature):
    def __init__(self, name, sprite, level, exp, hit_points, strength, agility, defense, accuracy, critical_hit, critical_hit_chance):
        super().__init__(name, sprite, level, exp, hit_points, strength, agility, defense, accuracy, critical_hit, critical_hit_chance, inventory)
        self.inventory = inventory
        