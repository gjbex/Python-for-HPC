# Convolution

Illustration of various concepts using a naive convolution algorithm
as an example.


## What is it?

1. `src`: source directory of C++ code.
   a. `convolution`: directory that contains the convolution and matrix code.
      1. `matrices.h`: definition of the Matrix class.
      1. `matrices.cpp` definition of methods for the Matrix class.
      1. `convolution.h`: decleartion of the convolution functions.
      1. `convolution.cpp`: implementation of the convolution functions.
      1. `CMakeLists.txt`: CMake file to build the shared library.
   a. `bindings`: directory that contains the pybind11 bindings
      for Matrix and convolve.
      1. `matrix_bind.cpp`: pybind11 bindings for the Matrix class.
      1. `convolve_bind.cpp`: pybind11 bindings for the convolve function.
         This uses the buffer protocol.
      1. `CMakeLists.txt`: CMake file to build the Python modules.
   a. `test_convolution.cpp`: C++ application to test the C++ convolution
      implementation.
   a. benchmark_convolution.cpp`: C++ application to benchmark the C++ convolution
      implementation.
   a. `CMakeLists.txt`: CMake file to build the library, modules and C++
      applications.
1. `CMakeLists.txt`: CMake file to build the library, modules and C++
   applications.
1. `test_convolution.py`: Python script to test and benchmark the generated
   modules.
