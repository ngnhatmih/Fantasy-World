import math

class Vector2D:

    def __init__(self, vector):
        if isinstance(vector, list) or isinstance(vector, tuple):
            self.x = vector[0]
            self.y = vector[1]
        elif isinstance(vector, Vector2D):
            self.x = vector.x
            self.y = vector.y
    
    def __add__(self, other):
        if isinstance(other, list) or isinstance(other, tuple):
            return Vector2D([self.x + other[0], self.y + other[1]])
        elif isinstance(other, Vector2D):
            return Vector2D([self.x + other.x, self.y + other.y])

    def __repr__(self):
        return f"[{self.x}, {self.y}]"

if __name__ == "__main__":
    v = Vector2D([2,3])
    u = Vector2D([3,5])
    print(v+u)