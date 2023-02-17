"""
Vector2d - класс, для представления двумерных векторов

Поддерживаемые операции:

Сложение::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)


Абсолютная величина::

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

Умножение на скаляр::

    >>> v * 3
    Vector(9, 12)
"""

class Vektor2D:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vektor2D(x, y)
    
    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vektor2D(x, y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)
    
    def __bool__(self):
        return (bool(self.x or self.y))

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

if __name__ == "__main__":
    v1 = Vektor2D(2, 1)
    v2 = Vektor2D(3, 4)
    print(v1 + v2)
    print(abs(v2))