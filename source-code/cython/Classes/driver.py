#!/usr/bin/env python

from points import Point, ColoredPoint

p = Point(1.0, -2.0)
print(p)
print(f'point = {p.x}, {p.y}')
print(p.distance())

p1 = ColoredPoint(1.0, -2.0, 'blue')
print(p1.color)
