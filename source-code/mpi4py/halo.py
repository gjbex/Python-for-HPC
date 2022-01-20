#!/usr/bin/env python

from argparse import ArgumentParser
from mpi4py import MPI
import numpy as np
import sys


def init_matrix(rank, n=4):
    matrix = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = rank + 0.01*(i*n + j + 1)
    return matrix


def matrix_to_str(matrix):
    matrix_list = matrix.tolist()
    row_strs = map(lambda row: ', '.join(['{:.2f}'.format(x) for x in row]),
                   matrix_list)
    return '\n'.join(row_strs)


def halo_to_str(halo):
    return ', '.join(['{:.2f}'.format(x) for x in halo.tolist()])


def halos_to_str(left, upper, right, lower):
    return '\n'.join([f'\t{x}' for x in [left, upper, right, lower]])


if __name__ == '__main__':
    arg_parser = ArgumentParser(description='illustrate halo exchange')
    arg_parser.add_argument('--n', type=int, default=4,
                            help='local matrix size')
    arg_parser.add_argument('--rows', type=int, default=2,
                            help='number of rows in Cartesian communicator')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='provide verbose output')
    options = arg_parser.parse_args()
    root = 0
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    matrix = init_matrix(rank, options.n)
    right_halo = np.zeros(options.n)
    left_halo = np.zeros(options.n)
    upper_halo = np.zeros(options.n)
    lower_halo = np.zeros(options.n)
    if size % options.rows == 0:
        rows = options.rows
        cols = size//options.rows
    else:
        if rank == root:
            msg = f'number of rows {options.rows} does not divide comm size {size}'
            print(f'number of rows {options.rows} does not divide comm size {size}',
                  file=sys.stderr)
        comm.Abort(1)
    cart_comm = comm.Create_cart([rows, cols])
    rank = cart_comm.Get_rank()
    print('rank {0:d}:\n{1}'.format(rank, matrix_to_str(matrix)))
    left, right = cart_comm.Shift(0, 1)
    up, down = cart_comm.Shift(1, 1)
    if options.verbose:
        print(f'rank {rank}, left = {left}, up = {up}, right = {right}, down = {down}')
    # note that the column data is stored non-contiguously, and has to be copied
    # before sending it
    send_buffer = np.array(matrix[:, 0]).copy()
    cart_comm.Sendrecv(send_buffer, left, recvbuf=right_halo, source=right)
    send_buffer = np.array(matrix[:, -1]).copy()
    cart_comm.Sendrecv(send_buffer, right, recvbuf=left_halo, source=left)
    # row data is contiguous and can be used as a sendbuffer without copying
    cart_comm.Sendrecv(matrix[0, :], up, recvbuf=lower_halo, source=down)
    cart_comm.Sendrecv(matrix[-1, :], down, recvbuf=upper_halo, source=up)
    halo_str = halos_to_str(left_halo, upper_halo, right_halo, lower_halo)
    print(f'rank {rank}\n{halo_str}')
