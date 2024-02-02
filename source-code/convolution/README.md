# Convolution

Convolution of an image using a kernel makes a nice problem to implement
using various HPC technologies.  It is conceptually simple enough to be used
as an exercise, yet computationally sufficiently challenging to make it
interesting.

To get you started, you get a
  * [Python](python) implementations, and
  * [C++](cpp) implementation. 


You can try to:

  * use numba,
  * use Cython,
  * use Swig to bind the C++ implementation,
  * use PyBind11 to bind the C++ implementation,
  * parallelize the code using Cython,
  * parallelize the code using multiprocessing,
  * parallelize and run the application on multiple nodes MPI.
