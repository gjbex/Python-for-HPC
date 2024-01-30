# Statistics

Illustration of how to use numpy arrays in pybind11.


## What is it?

1. `src/statistics/statistics.h`: declaration of a (simple) statistics
   analysis class.
1. `src/statistics/statistics.cpp`: definition of class methods.
1. `src/statistics/CMakeLists.txt`: CMake file to build a shared object.
1. `src/bindings/statistics_bind.cpp`: definition of the pybind11
   wrapper code.
1. `src/bindings/CMakeLists.txt`: CMake file to build the shared object
   that provides the Python module.
1. `CMakeLists.txt`: CMake file to build the extension.
1. `test.py`: Python scripts that uses the module.
