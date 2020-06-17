#!/usr/bin/env python

from argparse import ArgumentParser
from mpi4py import MPI
import sys
import time


def make_msg(value, nr_bytes):
    return f'{value:08d}'*(nr_bytes//8)


def make_float_msg(value, nr_bytes):
    return float(value)*(nr_bytes//8)


def acknowledge(comm):
    comm.barrier()
    rank = comm.Get_rank()
    size = comm.Get_size()
    print(f'process {rank} out of {size}')
    comm.barrier()


def pingpong(comm, nr_iters, msg_size):
    comm.barrier()
    rank = comm.Get_rank()
    size = comm.Get_size()
    for _ in range(nr_iters):
        for source in range(size):
            for dest in range(size):
                if (source != dest):
                    if rank == source:
                        start_time = time.time()
                        comm.send(make_msg(source, msg_size), dest=dest)
                        msg = comm.recv(source=dest)
                        end_time = time.time()
                        if msg != make_msg(dest, msg_size):
                            print(f'{rank} received {msg}, expected {dest}',
                                  file=sys.stderr)
                            comm.Abort(1)
                        print(f'{rank} -> {dest} pingpong: {end_time - start_time}')
                    if rank == dest:
                        start_time = time.time()
                        msg = comm.recv(source=source)
                        comm.send(make_msg(dest, msg_size), dest=source)
                        end_time = time.time()
                        if msg != make_msg(source, msg_size):
                            print(f'{rank} received {msg}, expected {source}',
                                  file=sys.stderr)
                            comm.Abort(1)
                        print(f'{rank} -> {source} pingpong: {end_time - start_time}')
    comm.barrier()
                    

def broadcast(comm, nr_iters, msg_size):
    comm.barrier()
    rank = comm.Get_rank()
    size = comm.Get_size()
    for _ in range(nr_iters):
        for root in range(size):
            msg = None
            if (rank == root):
                msg = make_msg(root, msg_size)
            start_time = time.time()
            msg = comm.bcast(msg, root=root)
            end_time = time.time()
            print(f'{root} -> {rank} bcast: {end_time - start_time}')
            if msg != make_msg(root, msg_size):
                print(f'{rank} received unexpected bcast message')
                comm.Abort(2)
    comm.barrier()


def scatter(comm, nr_iters, msg_size):
    comm.barrier()
    rank = comm.Get_rank()
    size = comm.Get_size()
    for _ in range(nr_iters):
        for root in range(size):
            msg = None
            if (rank == root):
                msg = [make_msg(dest, msg_size) for dest in range(size)]
            start_time = time.time()
            msg = comm.scatter(msg, root=root)
            end_time = time.time()
            print(f'{root} -> {rank} scatter: {end_time - start_time}')
            if msg != make_msg(rank, msg_size):
                print(f'{rank} received unexpected scatter message')
                comm.Abort(2)
    comm.barrier()


def gather(comm, nr_iters, msg_size):
    comm.barrier()
    rank = comm.Get_rank()
    size = comm.Get_size()
    for _ in range(nr_iters):
        for root in range(size):
            msg = make_msg(rank, msg_size)
            start_time = time.time()
            msg = comm.gather(msg, root=root)
            end_time = time.time()
            print(f'{root} -> {rank} gather: {end_time - start_time}')
            if (rank == root):
                if len(msg) != size:
                    print(f'{rank} received unexpected gather message')
                    comm.Abort(2)
                for i, msg in enumerate(msg):
                    if msg != make_msg(i, msg_size):
                        print(f'{rank} received unexpected gather message')
                        comm.Abort(2)
    comm.barrier()


def alltoall(comm, nr_iters, msg_size):
    comm.barrier()
    rank = comm.Get_rank()
    size = comm.Get_size()
    for _ in range(nr_iters):
        msg = [make_msg(rank, msg_size) for _ in range(size)]
        start_time = time.time()
        msg = comm.alltoall(msg)
        end_time = time.time()
        print(f'{rank} alltoall: {end_time - start_time}')
        if len(msg) != size:
            print(f'{rank} received unexpected alltoall message')
            comm.Abort(2)
        for i, msg in enumerate(msg):
            if msg != make_msg(i, msg_size):
                print(f'{rank} received unexpected alltoall message')
                comm.Abort(2)
    comm.barrier()


def reduce(comm, nr_iters, msg_size):
    comm.barrier()
    rank = comm.Get_rank()
    size = comm.Get_size()
    for _ in range(nr_iters):
        for root in range(size):
            msg = make_float_msg(rank, msg_size)
            start_time = time.time()
            msg = comm.reduce(msg, op=MPI.SUM, root=root)
            end_time = time.time()
            print(f'{root} -> {rank} reduce: {end_time - start_time}')
    comm.barrier()


def main():
    root = 0
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    if (rank == root):
        print(f'# acknowledgment')
    acknowledge(comm)
    arg_parser = ArgumentParser(description='MPI performance benchmark')
    arg_parser.add_argument('--nr_pingpongs', type=int, default=10,
                            help='number of ping-pong iterations to perform')
    arg_parser.add_argument('--pingpong_size', type=int, default=8,
                            help='number of bytes for ping-pong message')
    arg_parser.add_argument('--nr_bcasts', type=int, default=10,
                            help='number of broadcast iteration to perform')
    arg_parser.add_argument('--bcast_size', type=int, default=8,
                            help='number of bytes for broadcast message')
    arg_parser.add_argument('--nr_scatters', type=int, default=10,
                            help='number of scatter iteration to perform')
    arg_parser.add_argument('--scatter_size', type=int, default=8,
                            help='number of bytes for scatter message')
    arg_parser.add_argument('--nr_gathers', type=int, default=10,
                            help='number of gather iteration to perform')
    arg_parser.add_argument('--gather_size', type=int, default=8,
                            help='number of bytes for gather message')
    arg_parser.add_argument('--nr_alltoalls', type=int, default=10,
                            help='number of alltoall iteration to perform')
    arg_parser.add_argument('--alltoall_size', type=int, default=8,
                            help='number of bytes for alltoall message')
    arg_parser.add_argument('--nr_reduces', type=int, default=10,
                            help='number of reduce iteration to perform')
    arg_parser.add_argument('--reduce_size', type=int, default=8,
                            help='number of bytes for reduce message')
    options = arg_parser.parse_args()
    comm.barrier()
    if (rank == root):
        print(f'# {options.nr_pingpongs} ping-pong iterations, '
              f'size {options.pingpong_size}')
    comm.barrier()
    pingpong(comm, options.nr_pingpongs, options.pingpong_size)
    comm.barrier()
    if (rank == root):
        print(f'# {options.nr_bcasts} broadcast iterations, '
              f'size {options.bcast_size}')
    comm.barrier()
    broadcast(comm, options.nr_bcasts, options.bcast_size)
    comm.barrier()
    if (rank == root):
        print(f'# {options.nr_scatters} scatter iterations, '
              f'size {options.scatter_size}')
    comm.barrier()
    scatter(comm, options.nr_scatters, options.scatter_size)
    comm.barrier()
    if (rank == root):
        print(f'# {options.nr_gathers} gather iterations, '
              f'size {options.gather_size}')
    comm.barrier()
    gather(comm, options.nr_gathers, options.gather_size)
    comm.barrier()
    if (rank == root):
        print(f'# {options.nr_alltoalls} alltoall iterations, '
              f'size {options.alltoall_size}')
    comm.barrier()
    alltoall(comm, options.nr_alltoalls, options.alltoall_size)
    comm.barrier()
    if (rank == root):
        print(f'# {options.nr_reduces} reduce iterations, '
              f'size {options.reduce_size}')
    comm.barrier()
    reduce(comm, options.nr_reduces, options.reduce_size)
    comm.barrier()
    return 0


if __name__ == '__main__':
    sys.exit(main())
