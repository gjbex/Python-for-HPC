#!/usr/bin/env python

from argparse import ArgumentParser
import numpy as np
import sys

from julia import julia_set_omp_mod


def init_z_values(nr_points):
    real = np.linspace(-1.8, 1.8, nr_points)
    imag = np.linspace(-1.8, 1.8, nr_points)
    Real, Imag = np.meshgrid(real, imag)
    return np.asfortranarray(Real + Imag*1.0j)


def init_n_values(nr_points):
    return np.zeros((nr_points, nr_points), dtype=np.int32, order='F')


def main():
    arg_parser = ArgumentParser(description='compute julia set')
    arg_parser.add_argument('--n', type=int, default=100,
                            help='number of points')
    options = arg_parser.parse_args()
    z = init_z_values(options.n)
    n = init_n_values(options.n)
    julia_set_omp_mod.julia_compute(z, n)
    np.savetxt(sys.stdout, n, fmt='%4d')


if __name__ == '__main__':
    status = main()
    sys.exit(status)
