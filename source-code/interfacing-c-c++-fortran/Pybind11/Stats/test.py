#!/usr/bin/env python

import argparse
import numpy as np
import stats
import timeit


def compute_stats(data):
    my_stats = stats.Statistics()
    for value in data:
        my_stats.add(value)
    return my_stats

def main():
    parser = argparse.ArgumentParser(description='Compute statistics for a given number of random numbers')
    parser.add_argument('--n', type=int, default=10,
                        help='number of data values')
    parser.add_argument('--repetitions', type=int, default=1,
                        help='number of repetitions')
    parser.add_argument('--check', action='store_true',
                        help='check the results')
    args = parser.parse_args()
    data = np.random.uniform(size=args.n)
    time = timeit.timeit(lambda: compute_stats(data), number=args.repetitions)
    print(f'{time/args.repetitions:.6f} s (Statistics iterative mean)')
    time = timeit.timeit(lambda: stats.compute_stats(data), number=args.repetitions)
    print(f'{time/args.repetitions:.6f} s (Statistics numpy access mean)')
    time = timeit.timeit(lambda: data.mean(), number=args.repetitions)
    print(f'{time/args.repetitions:.6f} s (numpy mean)')
    if args.check:
        print()
        my_stats = compute_stats(data)
        print(f'{my_stats.mean()} (Statistics iterative mean)')
        my_stats = stats.compute_stats(data)
        print(f'{my_stats.mean()} (Statistics numpy access mean)')
        print(f'{data.mean()} (numpy mean)')

if __name__ == '__main__':
    main()
