#!/usr/bin/env python

import argparse
from build.src.bindings.convolve import convolve
import numpy as np
import timeit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_size', type=int, default=10, help='number of rows in the image')
    parser.add_argument('--kernel_size', type=int, default=3, help='number of rows in the kernel')
    parser.add_argument('--num_iter', type=int, default=1, help='number of iterations to run')
    args = parser.parse_args()

    # Create input image and kernel
    input_image = np.random.uniform(0.0, 1.0, size=(args.img_size, args.img_size))
    kernel = np.random.rand(args.kernel_size, args.kernel_size)
    result = np.empty((args.img_size + args.kernel_size - 1, args.img_size + args.kernel_size - 1))
    time = timeit.timeit(lambda: convolve(input_image, kernel, result), number=args.num_iter)
    print(f'Image size: {args.img_size}x{args.img_size}')
    print(f'Kernel size: {args.kernel_size}x{args.kernel_size}')
    print(f'Time: {time/args.num_iter:.6f} seconds')
    print(f'Sum: {np.sum(result)}')

if __name__ == '__main__':
    main()
