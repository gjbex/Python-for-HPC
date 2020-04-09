# Julia set

Implementatoin of the computation of the Julia set using Cython and Dask.

## What is it?

1. `julia_cython.pyx`: Cython implementation of computing a range of values.
1. `julia_cython_omp.pyx`: Cython OpenMP implementation of computing a range of
   values.
1. `setup.py`: Python build file for the Cython modules.
1. `Makefile`: make file to build the Cython modules.
1. `julia_set_dask.py`: Python driver program.
1. `julia_set_dask.pbs`: PBS script to run the computation.
1. `launch_scheduler.sh`: Bash script to launch the scheduler.
1. `launch_worker.sh`: Bash script to launch a worker.
