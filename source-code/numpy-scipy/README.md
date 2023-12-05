# Numpy and scipy

Some examples of numpy and scipy usage.  Mainly intended for benchmarking.

## What is it?

1. `svd.py`: Python script that reads a dataset representing a matrix in
  an HDF5 file.  It computes the Singular Value Decomposition (SVD) and
  reconstructs the original matrix from that.  Timings for HDF5 reads,
  SVD and matrix multiplications are printed.
1. `create_h5.py`: Python script to create an HDF5 file that can be used
   by `svd.py`.
1. `julia_set.ipynb`: Jupyter notebook to illustrate numpy type conversion.
1. `numpy_performance.ipynb`: Jupyter notebooks illustrating some performance
   issues with numpy.
1. `fancy_indexing.py`: Python script that tests performance of fancy indexing
   arrays in numpy.
