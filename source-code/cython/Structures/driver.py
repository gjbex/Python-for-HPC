#!/usr/bin/env python

import argparse

arg_parser = argparse.ArgumentParser(description='Driver for point modules')
arg_parser.add_argument('module', choices=['cython', 'pure_python'],
                        help='module to use')
options = arg_parser.parse_args()

if options.module == 'cython':
    import point_cython as point
elif options.module == 'pure_python':
    import point_pure as point

p = point.create(1.0, -2.0, 1)
print(p)
print('radius = {0}'.format(point.radius(p)))
point.project(p)
print(p)
