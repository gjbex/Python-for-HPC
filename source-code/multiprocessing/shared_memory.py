#!/usr/bin/env python

from argparse import ArgumentParser
from multiprocessing import Pool
from multiprocessing.managers import SharedMemoryManager
import numpy as np
import os
import sys

def increment(args):
    shmem, dtype, incr, i_min, i_max = args
    t_size = np.dtype(dtype).itemsize
    data = np.ndarray((i_max - i_min, ), dtype=dtype,
                      buffer=shmem.buf[t_size*i_min:t_size*i_max])
    for i in range(data.size):
        data[i] *= incr
    return os.getpid(), incr


def compute(array_size, pool_size, chunk_size, verbose=False):
    with SharedMemoryManager() as shmem_manager:
        with Pool(pool_size) as pool:
            dtype = np.int32
            t_size = np.dtype(dtype).itemsize
            shmem_data = shmem_manager.SharedMemory(size=t_size*array_size**2)
            data = np.ndarray((array_size, array_size), dtype=dtype,
                              buffer=shmem_data.buf)
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    data[i, j] = i*array_size + j
            args = [(shmem_data, np.int32, i + 1, i*chunk_size,
                     min((i + 1)*chunk_size, data.size))
                    for i in range(int(np.ceil(data.size/chunk_size)))]
            for result in pool.imap_unordered(increment, args):
                if verbose:
                    print(result)
            return data.copy()

if __name__ == '__main__':
    arg_parser = ArgumentParser(description='illustrating shared memory')
    arg_parser.add_argument('--pool_size', type=int, default=2,
                            help='pool size')
    arg_parser.add_argument('--array_size', type=int, default=10,
                            help='array size')
    arg_parser.add_argument('--chunk_size', type=int, default=10,
                            help='chunk size')
    arg_parser.add_argument('--sum_only', action='store_true',
                            help='only desplay sum of array elements')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='verbose output')
    options = arg_parser.parse_args()
    data = compute(array_size=options.array_size, pool_size=options.pool_size,
                   chunk_size=options.chunk_size, verbose=options.verbose)
    if options.sum_only:
        print(data.sum())
    else:
        np.savetxt(sys.stdout,data, fmt='%5d')
