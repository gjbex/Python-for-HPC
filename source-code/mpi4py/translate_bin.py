#!/usr/bin/env python

import argparse
import numpy as np


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="read and print MPI-IO data")
    arg_parser.add_argument('file', help='file to read')
    options = arg_parser.parse_args()
    data = np.fromfile(options.file)
    for value in data:
        print(value)
