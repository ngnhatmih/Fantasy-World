from entity import Entity

class Creature(Entity):
    def __init__(self, name, sprite, description, species, level, exp, hit_points, strength, agility, defense, accuracy, critical_hit, critical_hit_chance):
        super().__init__(name, sprite, description)
        self.species = species
        self.level = level
        self.exp = exp
        self.hit_points = hit_points
        self.strength = strength #physical power or damage output.
        self.agility = agility #speed or reflexes
        self.defense = defense
        self.accuracy = accuracy
        self.critical_hit = critical_hit #critical damage
        self.critical_hit_chance = critical_hit_chance
