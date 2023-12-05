from math import sqrt

class Point:
    
    _x: float
    _y: float
    
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def distance(self, other) -> float:
        return sqrt((self.x - other.x)*(self.x - other.x) + (self.y - other.y)*(self.y - other.y))
    
    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self._x = float(value)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        self._y = float(value)

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
