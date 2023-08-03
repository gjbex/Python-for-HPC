#!/usr/bin/env python

from argparse import ArgumentParser, FileType
import numpy as np
import re
import sys


def accumulate(data_file):
    regex = re.compile(r'^([a-z]+).+?(\d+\.\d+):\s+(\d+(?:\.\d+)(?:e[+-]\d+)?)')
    timings = {}
    times = {}
    for line in data_file:
        if match := regex.search(line):
            test = match[1]
            time = float(match[2])
            duration = float(match[3])
            if test not in timings:
                timings[test] = []
                times[test] = []
            timings[test].append(duration)
            times[test].append(time)
    return {test: np.array([times[test], timings[test]]).T for test in timings}


def print_stats(test, data):
    print(f'{test}:')
    print(f'    min:    {data.min()}')
    print(f'    median: {np.median(data)}')
    print(f'    mean:   {data.mean()}')
    print(f'    max:    {data.max()}')
    print(f'    stddev: {np.std(data)}')
    print(f'    n:      {len(data)}')


def main():
    arg_parser = ArgumentParser(description='analyze mpifitness data')
    arg_parser.add_argument('file', type=FileType('r'), help='file to analyse')
    options = arg_parser.parse_args()
    timings = accumulate(options.file)
    for test, data_list in timings.items():
        print_stats(test, data_list[:, 1])
    return 0


if __name__ == '__main__':
    sys.exit(main())
