#!/usr/bin/env python

from argparse import ArgumentParser, FileType
import numpy as np
import re
import sys


def accumulate(data_file):
    regex = re.compile(r'^([a-z]+).+?:\s+(\d+(?:\.\d+)(?:e[+-]\d+)?)')
    timings = dict()
    for line in data_file:
        match = regex.search(line)
        if match:
            test = match.group(1)
            time = float(match.group(2))
            if test not in timings:
                timings[test] = list()
            timings[test].append(time)
    return timings


def print_stats(test, data_list):
    print(f'{test}:')
    data = np.array(data_list)
    print(f'    min:    {data.min()}')
    print(f'    median: {np.median(data)}')
    print(f'    mean:   {data.mean()}')
    print(f'    max:    {data.max()}')
    print(f'    n:      {len(data)}')


def main():
    arg_parser = ArgumentParser(description='analyze mpifitness data')
    arg_parser.add_argument('file', type=FileType('r'), help='file to analyse')
    options = arg_parser.parse_args()
    timings = accumulate(options.file)
    for test, data_list in timings.items():
        print_stats(test, data_list)
    return 0


if __name__ == '__main__':
    sys.exit(main())
