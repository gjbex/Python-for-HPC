#!/usr/bin/env python

import argparse
import convolution
import numpy as np
import timeit

def create_image(rows, cols):
    return np.random.uniform(0.0, 1.0, size=(rows, cols))

def create_kernel(rows, cols):
    return np.ones((rows, cols))/(rows*cols)

def element_sum(matrix):
    return np.sum(matrix)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=1_000)
    parser.add_argument("--cols", type=int, default=1_000)
    parser.add_argument("--kernel_rows", type=int, default=7)
    parser.add_argument("--kernel_cols", type=int, default=7)
    args = parser.parse_args()

    print(f'Image size: {args.rows}x{args.cols}')
    print(f'Kernel size: {args.kernel_rows}x{args.kernel_cols}')

    image = create_image(args.rows, args.cols)
    kernel = create_kernel(args.kernel_rows, args.kernel_cols)


    print(f'Time: {timeit.timeit(lambda: convolution.convolve(image, kernel), number=1)} s')
    print(f'Sum: {element_sum(convolution.convolve(image, kernel))}')

if __name__ == "__main__":
    main()
