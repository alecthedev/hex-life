class Vector2:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self):
        if self == Vector2(0, 0):
            return Vector2(0, 0)
        return Vector2(self.x / self.magnitude(), self.y / self.magnitude())

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def distance_to(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

    def scale(self, factor):
        return Vector2(self.x * factor, self.y * factor)
