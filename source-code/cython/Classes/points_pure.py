import cython
from math import sqrt

@cython.cclass
class Point:
    
    x: cython.float
    y: cython.float
    
    def __init__(self, x: cython.float, y: cython.float) -> None:
        self.x = x
        self.y = y
        
    def distance(self) -> cython.float:
        return sqrt(self.x**2 + self.y**2)
    
    @property
    def x(self) -> cython.float:
        return self.x

    @x.setter
    def x(self, value: cython.float) -> None:
        self.x = float(value)

    @property
    def y(self) -> cython.float:
        return self.y

    @y.setter
    def y(self, value: cython.float) -> None:
        self.y = float(value)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


class ColoredPoint(Point):

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = str(value)

    def __str__(self):
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"
