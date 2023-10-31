# Primes
Motivating example for using Cython

## What is it?
1. `primes.py`: Python script to run either the Python, or the Cython
    version (both pyx and pure python) of copmuting a list of prime
    numbers less than the given number.
1. `primes_vanilla.py`: pure Python implementation of the primes function.
1. `primes_cython.pyx`: Cython implementation of the primes function.
1. `primes_pure_python.py`: Cython pure Python implementation of the
   primes function.
1. `setup.py`: Python build script.
1. `Makefile`: make file to build the extension.
1. `time_all.sh`: timings with hyperfine, **Note:** due to short runtimes
   these timings are donated by Python interpreter startup times and
   are hence skewed.
