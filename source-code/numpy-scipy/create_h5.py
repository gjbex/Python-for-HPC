#!/usr/bin/env python

import argparse
import h5py
import numpy as np
import sys


def main():
    arg_parser = argparse.ArgumentParser(description='create HDF5 file')
    arg_parser.add_argument('file', help='name of file to create')
    arg_parser.add_argument('--rows', type=int, default=10,
                            help='number of rows in the dataset')
    arg_parser.add_argument('--cols', type=int, default=10,
                            help='number of columns in the dataset')
    arg_parser.add_argument('--name', default='matrix',
                            help='name of the data set')
    options = arg_parser.parse_args()
    with h5py.File(options.file, 'w') as h5file:
        dataset = h5file.create_dataset(options.name, (options.rows, options.cols),
                                        dtype=np.float64)
        for row in range(options.rows):
            dataset[row, :] = np.random.uniform(size=(1, options.cols))
    return 0


if __name__ == '__main__':
    sys.exit(main())
