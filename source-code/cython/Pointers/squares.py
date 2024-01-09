#!/usr/bin/env python


import argparse

arg_parser = argparse.ArgumentParser(description='create a list of squares')
arg_parser.add_argument('--n', type=int, default=5,
                        help='number of squares to create')
arg_parser.add_argument('module', choices=['pure_python', 'cython'],
                        help='module to use for creating squares')
options = arg_parser.parse_args()

if options.module == 'pure_python':
    import pointers_pure as pointers
elif options.module == 'cython':
    import pointers_cython as pointers

print(pointers.squares(options.n))
