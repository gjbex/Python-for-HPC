#!/usr/bin/env python

import argparse
from functools import partial
import pathlib
import random
import re
import string
import sys


class SerialExecutor:

    def map(self, func, arg_list):
        result = list()
        for args in arg_list:
            result.append(func(args))
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass


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


def create_file(args):
    file_name, size, buffer_size = args
    with open(file_name, 'w') as file:
        for _ in range(size//buffer_size):
            buffer = ''.join(random.choices(string.ascii_lowercase, k=buffer_size))
            file.write(buffer)
        buffer = ''.join(random.choices(string.ascii_lowercase, k=(size % buffer_size)))
        file.write(buffer)


def read_file(args):
    file_name, buffer_size = args
    count = 0
    with open(file_name, 'r') as file:
        while (buffer := file.read(buffer_size)):
            count += len(buffer)
    return count


def remove_file(file_name):
    file = pathlib.Path(file_name)
    file.unlink()


def main():
    arg_parser = argparse.ArgumentParser(description='file read/write test')
    arg_parser.add_argument('basename', help='file basename')
    arg_parser.add_argument('--nr-files', type=int, default=1,
                            help='number of files to generate')
    arg_parser.add_argument('--file-size', default='4kb',
                            help='size of the files to be used')
    arg_parser.add_argument('--buffer-size', default='1kb',
                            help='buffer size for file operations')
    arg_parser.add_argument('--keep-files', action='store_true',
                            help='keep files that were created')
    arg_parser.add_argument('--shuffle', action='store_true',
                            help='shuffle file names between phases')
    arg_parser.add_argument('--mode', choices=['serial', 'threads', 'processes', 'mpi'],
                            default='serial', help='execution mode')
    arg_parser.add_argument('--nr-workers', type=int, default=1,
                            help='number of workers')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='verbose output')
    options = arg_parser.parse_args()

    # set parameters
    file_size = compute_size(options.file_size)
    if options.verbose:
        print(f'file size is {file_size}', file=sys.stderr)
    buffer_size = compute_size(options.buffer_size)

    # creae executor
    if options.verbose:
        print(f'buffer size is {buffer_size}', file=sys.stderr)
    if options.mode == 'serial':
        executor_cls = SerialExecutor
    elif options.mode == 'threads':
        import concurrent.futures
        executor_cls = partial(concurrent.futures.ThreadPoolExecutor, max_workers=options.nr_workers)
    elif options.mode == 'processes':
        import concurrent.futures
        executor_cls = partial(concurrent.futures.ProcessPoolExecutor, max_workers=options.nr_workers)
    elif options.mode == 'mpi':
        import mpi4py.futures
        executor_cls = mpi4py.futures.MPIPoolExecutor

    # create file names
    files = [f'{options.basename}_{file_id:06d}' for file_id in range(options.nr_files)]

    # create files
    if options.verbose:
        print(f'creating {len(files)} files', file=sys.stderr)
    with executor_cls() as executor:
        executor.map(create_file, ((file_name, file_size, buffer_size) for file_name in files))

    # if requested, shuffle files so that they are handled by a different thread/process
    if options.shuffle:
        random.shuffle(files)

    # read files
    if options.verbose:
        print(f'reading {len(files)} files', file=sys.stderr)
    with executor_cls() as executor:
        sizes = executor.map(read_file, ((file_name, buffer_size) for file_name in files))
        for size in sizes:
            if size != file_size:
                print(f"problem for file '{file_name}': {size} bytes read, {file_size} expected",
                      file=sys.stderr)

    # if requested, shuffle files so that they are handled by a different thread/process
    if options.shuffle:
        random.shuffle(files)

    # remove files
    if not options.keep_files:
        if options.verbose:
            print(f'reading {len(files)} files', file=sys.stderr)
        with executor_cls() as executor:
            executor.map(remove_file, files)

    if options.verbose:
        print('completed succesfully', file=sys.stderr)

    return 0


if __name__ == '__main__':
    sys.exit(main())
