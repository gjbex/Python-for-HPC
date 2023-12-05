import cython
from cython.cimports.libc.math import sqrt


@cython.cfunc
def _min_max_distance(points: cython.list) -> cython.tuple[cython.double, cython.double]:
    min_distance : cython.double = 2.0   
    max_distance : cython.double = 0.0
    for i in range(len(points)):
        p1 : Point = points[i]
        for j in range(i+1, len(points)):
            p2 : Point = points[j]
            distance = sqrt((p1._x - p2._x)*(p1._x - p2._x) + (p1._y - p2._y)*(p1._y - p2._y))
            if distance < min_distance:
                min_distance = distance
            if distance > max_distance:
                max_distance = distance
    return min_distance, max_distance


@cython.cclass
class Point:
    
    _x: cython.double
    _y: cython.double
    
    def __init__(self, x: cython.double, y: cython.double) -> None:
        self._x = x
        self._y = y
        
    @cython.ccall
    def distance(self, other: Point) -> cython.double:
        return sqrt((self._x - other._x)*(self._x - other._x) + (self._y - other._y)*(self._y - other._y))
    
    @staticmethod
    def min_max_distance(points: list) -> tuple[float, float]:
        return _min_max_distance(points)

    @property
    def x(self) -> cython.double:
        return self._x

    @x.setter
    def x(self, value: cython.double) -> None:
        self._x = float(value)

    @property
    def y(self) -> cython.double:
        return self._y

    @y.setter
    def y(self, value: cython.double) -> None:
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
