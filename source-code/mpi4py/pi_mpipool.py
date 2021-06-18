#!/usr/bin/env python

import argparse
from mpi4py.futures import MPIPoolExecutor
import numpy as np
import sys

def compute(args):
    x, end, n = args
    delta = (end - x)/n
    part = 0.0
    while x < end:
        part += np.sqrt(1.0 - x**2)
        x += delta
    return part*delta


def main():
    arg_parser = argparse.ArgumentParser(description='compute pi using MPIPoolExecutor')
    arg_parser.add_argument('--nr_points', type=int, default=1000,
                             help='number of points per work item')
    arg_parser.add_argument('--nr_parts', type=int, default=10,
                            help='number of workitems')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='show verbose output')
    options = arg_parser.parse_args()
    part_points = np.linspace(-1.0, 1.0, options.nr_parts + 1)
    args = [(start, end, options.nr_points) for start, end in zip(part_points[:-1], part_points[1:])]
    with MPIPoolExecutor() as executor:
        partial = executor.map(compute, args)
    print(f'quadrature pi = {2.0*sum(partial)}')
    print(f'real pi       = {np.pi}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
