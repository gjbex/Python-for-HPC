# Classes

Illustration of using Cython extension types (aka cdef classes).

## What is it?

1. `points.pyx`: implementation of a cdef class, and a Python
   child class thereof.
1. `driver.py`: Python script that uses both classes.
1. `setup.py`: Python installation file to build the Cython
   extension.
1. `Makefile`: make file to build the extension.
