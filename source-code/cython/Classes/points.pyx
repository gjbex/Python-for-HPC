from math import sqrt

cdef class Point:
    
    cdef double x, y
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self):
        return sqrt(self.x**2 + self.y**2)
    
    property x:
        def __get__(self):
            return self.x
        def __set__(self, value):
            self.x = float(value)
            
    property y:
        def __get__(self):
            return self.y
        def __set__(self, value):
            self.y = float(value)            


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
