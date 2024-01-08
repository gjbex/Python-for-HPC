#!/usr/bin/env python

# script to run various implementations of the convolution filter
# to compare their performance.
# The script has the following input parameters:
# --input_x: width of the input matrix
# --input_y: height of the input matrix
# --kernel_x: width of the kernel matrix
# --kernel_y: height of the kernel matrix
# --iterations: number of iterations to run
# --implementation: which implementation to run

import argparse
import numpy as np
import timeit
import sys

def main():
    parser = argparse.ArgumentParser(description='Run convolution filter')
    parser.add_argument('--input_x', type=int, default=100,
                        help='width of the input matrix')
    parser.add_argument('--input_y', type=int, default=100,
                        help='height of the input matrix')
    parser.add_argument('--kernel_x', type=int, default=9,
                        help='width of the kernel matrix')
    parser.add_argument('--kernel_y', type=int, default=9,
                        help='height of the kernel matrix')
    parser.add_argument('--iterations', type=int, default=1,
                        help='number of iterations to run')
    parser.add_argument('--implementation', type=str,
                        choices=['python', 'cython', 'cython_indexed', 'cython_no_checks'],
                        default='python',
                        help='which implementation to run')
    parser.add_argument('--check', action='store_true',
                        help='check the results')
    args = parser.parse_args()

    # Create input and kernel matrices
    input = np.random.rand(args.input_x, args.input_y)
    kernel = np.random.rand(args.kernel_x, args.kernel_y)

    # Run the requested implementation
    if args.implementation == 'python':
        from convolution import convolve
    elif args.implementation == 'cython':
        from convolution_cython import convolve
    elif args.implementation == 'cython_indexed':
        from convolution_cython_indexed import convolve
    elif args.implementation == 'cython_no_checks':
        from convolution_cython_no_checks import convolve

    # Measure the execution time
    time = timeit.timeit(lambda: convolve(input, kernel), number=args.iterations)
    print(f'Time: {time/args.iterations} s per iteration, {args.iterations} iterations')

    # Check the results
    if args.check:
        from convolution import convolve as convolve_python
        result_python = convolve_python(input, kernel)
        result = convolve(input, kernel)
        if np.allclose(result_python, result):
            print('Results are correct')
        else:
            print('Results are incorrect')
            sys.exit(1)

if __name__ == '__main__':
    main()
