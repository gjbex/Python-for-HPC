#!/usr/bin/env python

from argparse import ArgumentParser
import numpy as np
import pyximport
import timeit

pyximport.install(pyimport=True)
import array_sum_pure

def py_sum(a):
    total = 0.0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            total += a[i, j]
    return total

if __name__ == '__main__':
    arg_parser = ArgumentParser(description='compute array sum using '
                                            'pure, non-cythonized and pure cythonized implementations')
    arg_parser.add_argument('--n', type=int, default=10_000,
                            help='size (nxn array)')
    arg_parser.add_argument('--iter', type=int, default=10,
                            help='number of iterations')
    options = arg_parser.parse_args()
    a = np.ones((options.n, options.n))
    for func in [array_sum_pure.array_sum, py_sum]:
        total = 0.0
        start_time = timeit.default_timer()
        for iter_nr in range(options.iter):
            total += func(a)
        total_time = timeit.default_timer() - start_time
        print(f'{func.__qualname__:s}: {total_time:.6f} s ({total})')
