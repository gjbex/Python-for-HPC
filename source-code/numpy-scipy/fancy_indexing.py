#!/usr/bin/env python
#
# This script is intended to benchmark fancy indexiing with respect to
# for loops.
# 
# It takes the following commannd line arguments:
#   * --n: the numer of rows/columns in the matrix
#   * --r: the number of repetitions
#   * --algo: the algorithm(s) to use (either 'iterative' or 'fancy', or both)
#             This option can be specified multiple times, once for each of
#             the algorithms to use.
# For each repetition, the algorithm is timed to microsecond precision.
# For each repetition, the following values are printed to standard output:
#   * the name of the algorithm
#   * the number of rows/columns in the matrix
#   * the number of the repetition
#   * the time it took to run the algorithm, in microseconds.
# When all repetitions are done, the following values are printed to standard
# output:
#   * the name of the algorithm
#   * the number of rows/columns in the matrix
#   * the number of repetitions
#   * the average time it took to run the algorithm, in microseconds.
#   * the standard deviation of the time it took to run the algorithm, in
#     microseconds.
#   * the factor by which the value for the algorithm is slower than the
#     fastest algorithm.
#
# -----------------------------------------------------------------------------

import argparse
from collections import defaultdict
import numpy as np
import timeit


def setup(n):
    A = np.random.uniform(-1.0, 1.0, size=(n, n))
    B = np.random.uniform(-1.0, 1.0, size=A.shape)
    return A, B

def flip_signs_iterative(A, B):
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if B[i, j] > 0.5:
                A[i, j] *= -A[i, j]

def flip_signs_fancy(A, B):
    A[B > 0.5] *= -A[B > 0.5]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=100,
                        help='number of rows/columns in the matrix (default: 100')
    parser.add_argument('--r', type=int, default=1,
                        help='number of repetitions (default: 1')
    parser.add_argument('--algo', action='append', default=[],
                        choices=['iterative', 'fancy'],
                        help='algorithm(s) to use (default: none)')
    args = parser.parse_args()

    algorithms_lib = {
        'iterative': flip_signs_iterative,
        'fancy': flip_signs_fancy,
    }
    algorithms = [algorithms_lib[algo] for algo in args.algo]

    timings = defaultdict(list)
    print('algorithm,n,repetition,time')
    for i in range(1, args.r + 1):
        for algo in algorithms:
            A, B = setup(args.n)
            timings[algo].append(timeit.timeit(lambda: algo(A, B), number=1))
            print(f'{algo.__name__},{args.n},{i},{timings[algo][-1]:.6f}')
    print('summary:')
    min_time = min([np.mean(timings[algo]) for algo in algorithms])
    print('  algorithm,n,repetitions,mean,std,relative')
    for algo in algorithms:
        print(f'  {algo.__name__},{args.n},{args.r},{np.mean(timings[algo]):.6f},{np.std(timings[algo]):.6f},{np.mean(timings[algo]) / min_time:.2f}')

if __name__ == '__main__':
    main()
