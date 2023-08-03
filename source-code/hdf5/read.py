#!/usr/bin/env python

from argparse import ArgumentParser
import h5py
from mpi4py import MPI
import numpy as np
import sys


def read_data(data_set, data_size, offset, slice_size, comm, is_verbose=True):
    total = 0.0
    for _ in range(data_size//slice_size):
        total += np.sum(data_set[offset:offset + slice_size])
        offset += slice_size
    if data_size % slice_size != 0:
        slice_size = data_size % slice_size
        total += np.sum(data_set[offset:offset + slice_size])
    return total
    
    
def main():
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size
    root = 0

    if rank == root:
        arg_parser = ArgumentParser(description='read HDF5 file and sum all values in dataset')
        arg_parser.add_argument('file', help='HDF5 file to read')
        arg_parser.add_argument('--slice', type=int, default=1,
                                help='number of float64 values for a single read')
        arg_parser.add_argument('--verbose', action='store_true', help='verbose output')
        options = arg_parser.parse_args()
        file_name = options.file
        slice_size = options.slice
        is_verbose = options.verbose
    else:
        file_name = None
        slice_size = None
        is_verbose = None

    file_name = comm.bcast(file_name, root=root)
    slice_size = comm.bcast(slice_size, root=root)
    is_verbose = comm.bcast(is_verbose, root=root)

    with h5py.File(file_name, 'r', driver='mpio', comm=comm) as h5file:
        data_set = h5file.get('data')
        data_size = data_set.size//size
        offset = rank*data_size
        if rank == size - 1 and data_set.size % size != 0:
            data_size += data_set.size % size
        if is_verbose:
            print(f'rank {rank} at {offset} reads {data_size} float64 values, slice {slice_size}',
                  file=sys.stderr)
        value = read_data(data_set, data_size, offset, slice_size, comm, is_verbose)
        total = comm.reduce(value, op=MPI.SUM, root=root)
        if rank == root:
            print(f'total value = {total}')

    return 0

if __name__ == '__main__':
    sys.exit(main())
