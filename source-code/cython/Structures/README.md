# Structues

It is easy to define structures in Cython and pure Python
syntax.


## What is it?

1. `point_cython.pyx`: Cython file that defines structure and
   some functions that use this structure.
1. `point_pure.py`: pure Python file that defines structure and
   some functions that use this structure.
1. `setup.py`: Python setup file to build the Cython extensions.
1. `Makefile`: make file to build the Cython extensions.
1. `driver.py`: Python script to illustrate the use of the
   structure type, either the Cython or the pure Python version
   can be selected.
