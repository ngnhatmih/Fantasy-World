from entity import Entity

class Item(Entity):
    def __init__(self, name, sprite, description):
        super().__init__(name, sprite, description)