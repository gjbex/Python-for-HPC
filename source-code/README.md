# Source code

This is source code that is either used in the presentation, or was developed
to create it.  There is some material not covered in the presentation as well.


## Requirements

* Python version: at least 3.6
* Packages (names listed taht can be used with `pip` or `conda` to install):
  * cython
  * dask
  * numpy
  * numexpr
  * scipy
  * matplotlib
  * mpi4py
  * pytables
  * jupyter
  * ipywidgets

* For the GPU code:
  * pycuda
  * scikit-cuda


## What is it?

1. `cython`: illustrations of how to use Cython to speed up Python.
1. `dask`: examples of how to use dask for distributed computing.
1. `interfaciing-c-c++-fortran`: illustrations of ctypes, SWIG and
   f2py to interface with C, C++ and Fortran code.
1. `ising`: example of speeding up a Python simulation by wrapping
   C++ code using SWIG.
1. `mpi4py`: illustrations of distributed programming using MPI.
1. `multiprocessing`: illustrations of multithreaded programming
   using multiprocessing.
1. `numba`: illustration of using the numba library.
1. `profiling`: some illustrations and how-to on profiling a Python
   application.
1. `pyspark`: illustrations of using PySpark.
1. `hdf5`: examples of parallel I/O using HDF5.
1. `numpy-scipy`: some numpy/scipy codes for benchmakring.
1. `pypy`: code to experiment with the Pypy interpreter.
1. `file-formats`: influcence of file formats on performance.
1. `gpu`: some examples of using GPUs.
