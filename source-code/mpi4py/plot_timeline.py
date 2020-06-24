#!/usr/bin/env python

from argparse import ArgumentParser, FileType
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from analyze_mpifitness_data import accumulate


def main():
    arg_parser = ArgumentParser(description='plot MPI time distirbution')
    arg_parser.add_argument('--file', required=True, type=FileType('r'),
                            help='file to plot data from')
    arg_parser.add_argument('--test', required=True,
                            choices=['pingpong', 'bcast', 'scatter', 'gather',
                                     'alltoall', 'reduce'],
                            help='test to visualize')
    arg_parser.add_argument('--log', action='store_true', help='use log x-axis')
    options = arg_parser.parse_args()
    timings = accumulate(options.file)
    data = timings[options.test]
    grid = sns.scatterplot(x=(data[:, 0] - data[0, 0]), y=data[:, 1], alpha=0.6)
    if options.log:
        grid.set(yscale='log')
    grid.set(title=options.test)
    plt.show()
    return 0


if __name__ == '__main__':
    sys.exit(main())
