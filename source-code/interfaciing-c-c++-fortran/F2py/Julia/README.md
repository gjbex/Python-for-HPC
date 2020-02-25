# Julia set

Illustration of using f2py to interface with OpenMP code.

## What is it?

1. `julia_set_mod.f90`: Fortran module defining a function that computes a
   single point of a Julia set.

1. `julia_set_omp_mod.f90`: Fortran module that computes a Julia set
   parallelized with OpenMP.
1. `julia_set.py`: Python script that initlalizes the arrays and computes
   the Julia set using the Fortran implementation.
1. `Makefile`: make file to build the shared library.
1. `show_julia_set.py`: Python script to visualize the result.
