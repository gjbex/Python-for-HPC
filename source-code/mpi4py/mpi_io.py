#!/usr/bin/env python

import argparse
from mpi4py import MPI
import numpy as np
import re
import time


def compute_size(size_str):
    if (match := re.match(r'\s*(\d+)\s*([a-z]+)?', size_str, re.IGNORECASE)) is not None:
        size = int(match.group(1))
        if match.group(2):
            units = match.group(2).lower()
            if units == 'b':
                pass
            elif units == 'kb':
                size *= 1024
            elif units == 'mb':
                size *= 1024**2
            elif units == 'gb':
                size *= 1024**3
            elif units == 'tb':
                size *= 1024**4
            else:
                raise ValueError(f"invalid unit in size expression: '{size_str}'")
        return size
    else:
        raise ValueError(f"invalid size expression: '{size_str}'")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='write a file using MPI-IO')
    arg_parser.add_argument('--file', required=True,
                            help='file name to write')
    arg_parser.add_argument('--size', default='100mb',
                            help='file size to write')
    options = arg_parser.parse_args()

    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()
    total_file_size = compute_size(options.size)//8
    data_size = total_file_size//comm_size
    offset = comm_rank*data_size*8

    start_val = comm_rank*data_size
    end_val = (1 + comm_rank)*data_size
    if comm_rank == comm_size - 1:
        end_val += total_file_size % comm_size
    data = np.arange(start_val, end_val, 1.0)

    mode = MPI.MODE_WRONLY | MPI.MODE_CREATE
    start_time = time.time()
    file = MPI.File.Open(comm, options.file, mode)
    file.Write_at_all(offset, data)
    file.Close()
    end_time = time.time()
    total_time = end_time - start_time
    print(f'{comm_rank}, {total_time} s, {compute_size(options.size)/(total_time*2**20):.3f} MB/s') 
