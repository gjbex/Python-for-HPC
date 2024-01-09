import cython
import math

Point = cython.struct(
    x=cython.double,
    y=cython.double,
    id=cython.int
)

def create(x: cython.double, y: cython.double,  id: cython.int) -> Point:
    point: Point
    point.x = x
    point.y = y
    point.id = id
    return point

def radius(point: Point) -> cython.double:
    return math.sqrt(point.x**2 + point.y**2)

def azimuth(point: Point) -> cython.double:
    return math.atan2(point.y, point.x)

def project(point: Point) -> None:
    r: cython.double = radius(point)
    point.x /= r
    point.y /= r
    print(point)
