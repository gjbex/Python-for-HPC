# Numpy and scipy

Some examples of numpy and scipy usage.  Mainly intended for benchmarking.

## What is it?

1. svd.py`: Python script that reads a dataset representing a matrix in
  an HDF5 file.  It computes the Singular Value Decomposition (SVD) and
  reconstructs the original matrix from that.  Timings for HDF5 reads,
  SVD and matrix multiplications are printed.
