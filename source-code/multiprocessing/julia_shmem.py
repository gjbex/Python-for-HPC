#!/usr/bin/env python

from argparse import ArgumentParser
from collections import Counter
import math
import multiprocessing as mp
from multiprocessing.managers import SharedMemoryManager
import numpy as np
import os
import sys


def init_z(z_buf):
    nr_points = math.isqrt(z_buf.size)
    x = np.linspace(-1.8, 1.8, nr_points)
    y = np.linspace(-1.8j, 1.8j, nr_points)
    X, Y = np.meshgrid(x, np.flip(y))
    z = X + Y
    for i in range(z.shape[0]):
        for j in range(z.shape[1]):
            z_buf[i*z.shape[1] + j] = z[i, j]


def init_n(n_buf):
    for i in range(n_buf.size):
        n_buf[i] = 0


def compute_partial_julia(args):
    z_shmem, n_shmem, idx_begin, idx_end, max_iters, max_norm = args
    z_sizeof = np.dtype(np.complex).itemsize
    z = np.ndarray((idx_end - idx_begin, ), dtype=np.complex,
                   buffer=z_shmem.buf[z_sizeof*idx_begin:z_sizeof*idx_end])
    n_sizeof = np.dtype(np.int32).itemsize
    n = np.ndarray((idx_end - idx_begin, ), dtype=np.int32,
                   buffer=n_shmem.buf[n_sizeof*idx_begin:n_sizeof*idx_end])
    for i, z_value in enumerate(z):
        while (n[i] <= max_iters and np.abs(z_value) <= max_norm):
            z_value = z_value**2 - 0.622772 + 0.42193j
            n[i] += 1
    return os.getpid()


def compute_julia(nr_points=100, pool_size=2, work_size=15, verbose=False,
                  max_iters=255, max_norm=2.0):
    size = nr_points**2
    with SharedMemoryManager() as shmem_mgr:
        with mp.Pool(pool_size) as pool:
            z_shmem = shmem_mgr.SharedMemory(size=16*size)
            z_buf = np.ndarray((size, ), dtype=np.complex, buffer=z_shmem.buf)
            init_z(z_buf)
            n_shmem = shmem_mgr.SharedMemory(size=4*size)
            n_buf = np.ndarray((size, ), dtype=np.int32, buffer=n_shmem.buf)
            init_n(n_buf)
            args = [(z_shmem, n_shmem, i*work_size, min(z_buf.size, (i + 1)*work_size),
                     max_iters, max_norm)
                    for i in range(int(np.ceil(z_buf.size/work_size)))] 
            if verbose:
                print(args, file=sys.stderr)
            pid_counter = Counter()
            for pid in pool.imap_unordered(compute_partial_julia, args):
                pid_counter[pid] += 1
            if verbose:
                print(pid_counter, file=sys.stderr)
            return n_buf.copy().reshape(nr_points, nr_points)


def main():
    arg_parser = ArgumentParser(description='compute pi')
    arg_parser.add_argument('--pool_size', type=int, default=2, help='pool size')
    arg_parser.add_argument('--work_size', type=int, default=10,
                            help='number of points per work item')
    arg_parser.add_argument('--nr_points', type=int, default=10,
                            help='size of the image n x n')
    arg_parser.add_argument('--verbose', action='store_true', help='verbose output')
    options = arg_parser.parse_args()
    constructor = None
    n = compute_julia(nr_points=options.nr_points, pool_size=options.pool_size,
                      work_size=options.work_size, verbose=options.verbose)
    np.savetxt(sys.stdout, n, fmt='%3d')
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
