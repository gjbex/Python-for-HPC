#!/usr/bin/env python

import argparse
import itertools
import pyximport
pyximport.install(pyimport=True, language_level='3str')
from points_pure import Point
import random


def main():
    arg_parser = argparse.ArgumentParser(description='compute distances')
    arg_parser.add_argument('--n', type=int, default=10,
                            help='number of points')
    options = arg_parser.parse_args()
    points = [Point(random.random(), random.random()) for _ in range(options.n)]
    min_distance = 2.0
    max_distance = 0.0
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            d = p1.distance(p2)
            min_distance = min(d, min_distance)
            max_distance = max(d, max_distance)
    print(f'min. distance: {min_distance}')
    print(f'max. distance: {max_distance}')

if __name__ == '__main__':
    main()
