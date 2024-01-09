# Pointers
Simple example of using pointers in Cython code.

## What is it?
1. `pointers_cython.pyx`: Cython code that computes a list of squares
   using a cdef function that increments an integer value referred to
   by a pointer.
1. `pointers_pure.pyx`: pure Python code that computes a list of squares
   using a cfunc function that increments an integer value referred to by
   a pointer.
1. `setup.py`: Python build script.
1. `Makefile`: make file to build the extension.
1. `squares.py`: script to load one of the compiled module, and compute
   the squares of the first few positive integers.
