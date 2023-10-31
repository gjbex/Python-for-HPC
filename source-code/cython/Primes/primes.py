#!/usr/bin/env python

from argparse import ArgumentParser
import sys


if __name__ == '__main__':
    arg_parser = ArgumentParser(description='compute primes')
    arg_parser.add_argument('version', choices=['python', 'cython', 'pure_python'],
                            help='version to run')
    arg_parser.add_argument('--n', type=int, default=10,
                            help='number of primes')
    options = arg_parser.parse_args()
    if options.version == 'python':
        from primes_vanilla import primes
    elif options.version == 'cython':
        from primes_cython import primes
    elif options.version == 'pure_python':
        from primes_pure_python import primes
    results = primes(options.n)
    print(', '.join(map(str, results)))
