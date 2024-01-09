#!/usr/bin/env python

from argparse import ArgumentParser
import array

DEFAULT_SIZE = 10

arg_parser = ArgumentParser(description='test Cython errors')
arg_parser.add_argument('--m', type=int, default=0, help='lower bound')
arg_parser.add_argument('--n', type=int, default=DEFAULT_SIZE,
                        help='upper bound')
arg_parser.add_argument('--size', type=int, default=DEFAULT_SIZE,
                        help='array size')
arg_parser.add_argument('--implementation', choices=['pure', 'cython'],
                        default='cython', help='implementation to use')
options = arg_parser.parse_args()
if options.implementation == 'cython':
    from average import average, average_no_except
elif options.implementation == 'pure':
    from average_pure import average, average_no_except
data = array.array('d', list(range(options.size)))
print('with except:')
try:
    print(average(data, options.m, options.n))
except Exception as e:
    print('caught exception {0}: {1}'.format(str(e.__class__), str(e)))
print('without except:')
try:
    print(average_no_except(data, options.m, options.n))
    print('no exception caught')
except Exception as e:
    print('caught exception {0}: {1}'.format(e.__class__, str(e)))
