#!/usr/bin/env python

from argparse import ArgumentParser
from distributed import Client, Future
import numpy as np
import os
import sys
import time


def init_julia(re, im, n):
    '''Initialize the complex domain.

    Positional arguments:
    re -- minimum and maximum real value as 2-tuple
    im -- minimum and maximum imaginary value as 2-tuple
    n -- number of real and imaginary points as 2-tuple
    '''
    re_vals, im_vals = np.meshgrid(
            np.linspace(re[0], re[1], n[0]),
            np.linspace(im[0], im[1], n[1])
            )
    domain = re_vals + im_vals*1j
    return domain.flatten()


def init_pyx(dask_worker):
    import pyximport
    pyximport.install()
    sys.path.insert(0, os.getcwd())
#    sys.path.insert(0, '/scratch/leuven/301/vsc30140/julia_set/')
    from julia_cython import julia_set


def init_omp_pyx(dask_worker):
    import pyximport
    pyximport.install()
    sys.path.insert(0, os.getcwd())
#    sys.path.insert(0, '/scratch/leuven/301/vsc30140/julia_set/')
    from julia_cython_omp import julia_set



if __name__ == '__main__':
    arg_parser = ArgumentParser(description='Compute julia set')
    arg_parser.add_argument('--re_min', type=float, default=-1.8,
                            help='minimum real value')
    arg_parser.add_argument('--re_max', type=float, default=1.8,
                            help='maximum real value')
    arg_parser.add_argument('--im_min', type=float, default=-1.8,
                            help='minimum imaginary value')
    arg_parser.add_argument('--im_max', type=float, default=1.8,
                            help='maximum imaginary value')
    arg_parser.add_argument('--max_norm', type=float, default=2.0,
                            help='maximum complex norm for z')
    arg_parser.add_argument('--n_re', type=int, default=100,
                            help='number of points on the real axis')
    arg_parser.add_argument('--n_im', type=int, default=100,
                            help='number of points on the imaginary axis')
    arg_parser.add_argument('--max_iters', type=int, default=300,
                            help='maximum number of iterations')
    arg_parser.add_argument('--implementation', default='python',
                            choices=['python', 'cython', 'cython_omp'],
                            help='implementation to use')
    arg_parser.add_argument('--partitions', type=int, default=100,
                            help='number of partitions for dask workers')
    arg_parser.add_argument('--host', required=True,
                            help='hostname of the dask scheduler')
    arg_parser.add_argument('--port', type=int, required=True,
                            help='port of the dask scheduler')
    options = arg_parser.parse_args()
    client = Client(f'{options.host}:{options.port:d}')
    if options.implementation == 'python':
        from julia_python import julia_set
    elif options.implementation == 'cython':
        from julia_cython import julia_set
        client.register_worker_callbacks(init_pyx)
    elif options.implementation == 'cython_omp':
        from julia_cython_omp import julia_set
        client.register_worker_callbacks(init_omp_pyx)
    else:
        msg = '{0} version not implemented\n'
        sys.stderr.write(msg.format(options.implementation))
        sys.exit(1)
    
    domain = init_julia(
            (options.re_min, options.re_max),
            (options.im_min, options.im_max),
            (options.n_re, options.n_im)
            )
    domains = np.array_split(domain, options.partitions)
    iterations = np.array_split(np.zeros(options.n_re*options.n_im,
                                         dtype=np.int32), options.partitions)
    start_time = time.time()
    futures = client.map(julia_set, domains, iterations)
    results = client.gather(futures)
    end_time = time.time()
    print('compute time = {0:.6f} s'.format(end_time - start_time))
    np.savetxt('julia.txt', np.concatenate(results).reshape(options.n_re,
                                                            options.n_im))
