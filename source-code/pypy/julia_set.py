#!/usr/bin/env python

import argparse
import numpy as np
import sys
import time


def julia_set_iteration(z, c):
    i = 0
    while i < 255 and abs(z) < 2.0:
        z = z**2 + c
        i += 1
    return i

def julia_set(n, c):
    result = np.empty((n, n), dtype=np.uint8)
    delta = 2.0*1.8/n
    for i in range(n):
        z_re = -1.8 + i*delta
        for j in range(n):
            z_im = -1.8 + j*delta
            result[i, j] = julia_set_iteration(complex(z_re, z_im), c)
    return result


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='compute JUlia set')
    arg_parser.add_argument('n', type=int, help='number of points')
    options = arg_parser.parse_args()
    c = complex(0.4, 0.6)
    start = time.time()
    julia = julia_set(options.n, c)
    end = time.time()
    print(f'compute time: {end - start} s', file=sys.stderr)
    np.savetxt(sys.stdout, julia)
