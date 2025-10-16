#!/usr/bin/env python

import multiprocessing
import sys
import numpy as np

from runner import UnknownQuantityError


def _do_run(args):
    run_nr, is_verbose, runner, ising_spec = args
    ising_cls, ctor_args, base_seed = ising_spec
    ising = ising_cls(*ctor_args)
    if base_seed is not None:
        ising.init_random(base_seed + run_nr - 1)
    if is_verbose > 0:
        sys.stderr.write('# run {0:d}\n'.format(run_nr))
    runner.set_system(ising)
    runner.run()
    quantities = {}
    for quantity in runner.quantities():
        quantities[quantity] = runner.get(quantity)
    return quantities


class Averager(object):

    def __init__(self, runner, ising, is_verbose=1):
        self._is_verbose = is_verbose
        self._runner = runner
        self._ising = ising
        self._quantities = {}
        nr_cpus = multiprocessing.cpu_count()
        if is_verbose > 0:
            sys.stderr.write('# using {0:d} cores\n'.format(nr_cpus))
        self._pool = multiprocessing.Pool(nr_cpus)

    def average(self, runs, base_seed=None):
        run_input = []
        ctor_args = (self._ising.N(), self._ising.J(),
                     self._ising.H(), self._ising.T())
        ising_spec = (self._ising.__class__, ctor_args, base_seed)
        for run in range(1, runs + 1):
            runner = self._runner.clone()
            runner.set_system(None)  # Avoid shipping non-picklable backends.
            run_input.append((run, self._is_verbose, runner, ising_spec))
        results = self._pool.map(_do_run, run_input)
        for result in results:
            for quantity in result:
                if quantity not in self.quantities():
                    self._quantities[quantity] = []
                self._quantities[quantity].append(result[quantity])

    def quantities(self):
        return self._quantities.keys()

    def get(self, quantity):
        if quantity in self._quantities:
            result = {}
            if type(self._quantities[quantity][0]) == dict:
                for dictionary in self._quantities[quantity]:
                    for key in dictionary:
                        if key not in result:
                            result[key] = 0
                        result[key] += dictionary[key]
                for key in result:
                    result[key] /= float(len(self._quantities[quantity]))
            else:
                result['mean'] = np.mean(self._quantities[quantity])
                result['std'] = np.std(self._quantities[quantity])
                result['min'] = np.min(self._quantities[quantity])
                result['max'] = np.max(self._quantities[quantity])
                result['N'] = len(self._quantities[quantity])
            return result
        else:
            raise UnknownQuantityError(quantity)
