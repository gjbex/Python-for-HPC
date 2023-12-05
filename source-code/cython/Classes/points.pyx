from libc.math cimport sqrt

cdef class Point:
    
    cdef double _x, _y
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    cpdef distance(self, other):
        return sqrt((self._x - other._x)**2 + (self._y - other._y)**2)
    
    property x:
        def __get__(self):
            return self._x
        def __set__(self, value):
            self._x = float(value)
            
    property y:
        def __get__(self):
            return self._y
        def __set__(self, value):
            self._y = float(value)            


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
