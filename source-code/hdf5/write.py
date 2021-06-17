#!/usr/bin/env python

from argparse import ArgumentParser
from mpi4py import MPI
import h5py
import numpy as np
import sys


def write_data(data_set, data_size, offset, slice_size, comm, is_verbose=False):
    value_min = comm.rank
    value_delta = 1.0/data_size
    value_max = value_min + value_delta*(slice_size - 1)
    for slice_nr in range(data_size//slice_size):
        data = np.linspace(value_min, value_max, slice_size)
        if is_verbose:
            print(f'rank {comm.rank}: at {slice_nr*slice_size} writing {data.shape} values '
                  f'from {data[0]} to {data[-1]}', file=sys.stderr)
        data_set[offset:offset + slice_size] = data
        value_min += slice_size*value_delta
        value_max += slice_size*value_delta
        offset += slice_size
    if data_size % slice_size != 0:
        nr_values = data_size % slice_size
        value_max = value_min + value_delta*(nr_values - 1)
        data = np.linspace(value_min, value_max, nr_values)
        if is_verbose:
            print(f'rank {comm.rank}: at {slice_nr*slice_size} writing {data.shape} values '
                  f'from {data[0]} to {data[-1]}', file=sys.stderr)
        data_set[offset:offset+nr_values] = data



def main():
    root = 0
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size
    if rank == root:
        arg_parser = ArgumentParser(description='write data to an HDF5 file')
        arg_parser.add_argument('file', help='file name to write to')
        arg_parser.add_argument('--size', type=int, default=2*3*4*5,
                                help='total number of float64 values to write')
        arg_parser.add_argument('--slice', type=int, default=1,
                                help='number of float64 values to write in single write')
        arg_parser.add_argument('--verbose', action='store_true',
                                help='print verbose output')
        options = arg_parser.parse_args()
        if options.slice*size > options.size:
            print(f'not enough work: {options.size} items for {size} processes, writing {options.slice} each',
                  file=sys.stderr)
            MPI.abort(1)
        file_name = options.file
        total_size = options.size
        slice_size = options.slice
        is_verbose = options.verbose
    else:
        file_name = None
        total_size = None
        slice_size = None
        is_verbose = None
    file_name = comm.bcast(file_name, root=root)
    total_size = comm.bcast(total_size, root=root)
    slice_size = comm.bcast(slice_size, root=root)
    is_verbose = comm.bcast(is_verbose, root=root)
    data_size = total_size//size
    offset = rank*data_size
    if rank == size - 1 and total_size % size != 0:
        data_size += total_size % size

    if is_verbose:
        print(f'process {rank} writing {data_size} float64 values to \'{file_name}\' at {offset}',
              file=sys.stderr)
    
    with h5py.File(file_name, 'w', driver='mpio', comm=comm) as h5file:
        data_set = h5file.create_dataset('data', (total_size, ), 'f')
        write_data(data_set, data_size, offset, slice_size, comm, is_verbose)

    return 0

if __name__ == '__main__':
    sys.exit(main())
