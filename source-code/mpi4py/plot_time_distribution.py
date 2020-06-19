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
    arg_parser.add_argument('--bins', type=int, default=5,
                            help='number of bins in histogram')
    arg_parser.add_argument('--rug', action='store_true', help='show rug')
    options = arg_parser.parse_args()
    timings = accumulate(options.file)
    if options.rug:
        sns.distplot(timings[options.test], rug=True, hist=False)
    else:
        sns.distplot(timings[options.test], bins=options.bins)
    plt.show()
    return 0


if __name__ == '__main__':
    sys.exit(main())
