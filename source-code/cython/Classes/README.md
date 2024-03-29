# Classes

Illustration of using Cython extension types (aka cdef classes).

## What is it?

1. `points.pyx`: implementation of a cdef class, and a Python
   child class thereof.
1. `points_pure.py`: implementation in Cython's pure Python
   syntax.
1. `points_python.py`: Python implementation of the class.
1. `driver.py`: Python script that uses both classes.
1. `setup.py`: Python installation file to build the Cython
   extension.
1. `distances_cython.py`: Python script to compute distances between
   points using Cython class.
1. `distances_python.py`: Python script to compute distances between
   points using Python class.
1. `distances_internal.py`: Python script to compute distances between
   points using Cython class, computing the distances using a static
   class method..
1. `Makefile`: make file to build the extension.
