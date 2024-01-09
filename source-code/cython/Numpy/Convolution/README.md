# Convolution

Illustration of how to improve perfomance when using numpy arrays in Cython
by doing indexing right.  The algorithm used is a naive implementation of
convolution.


## What is it?

1. `convolution.py`: Python implementation of the algorithm (uses numpy).
1. `convolution.pyx`: Cython implementation that adds types.
1. `convolution_indexed.pyx`: Cython implementation that adds
   numpy array element types and indexing information.
1. `convolution_no_checks.pyx`: Cython implementation that adds
   function decorator to avoid index checks for numpy arrays.
1. `setup.py`: script to build the extensions.
1. `Makefile`: make file to conveniently build the extensions.
1. `driver.py`: Python scripts to run benchmark tests on the various
   implementations.
