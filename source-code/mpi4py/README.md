# Mpi4py
Distributed parallel programs can be developed using this library (not
in Python's starndard library, requires that an MPI library is installed).
It follows the MPI standard to some degree, but simplifies in many places,
making development easy, at the price of performace.
Not to be advised when interprocess communication is fine-grained with
respect to communication given (much) larger overhead when compared with
C/C++ or Fortran implementations.

## What is it?
1. `all_to_all.py`: simple example of an all-to-all comminication.
1. `halo.py`: halo exchange example, illustrates 2D cartesian grid
    communicator, Sendrecv.
1. `pi.py`: implementation for computing pi as suggested in the slides.
1. `reduce.py`: example of numpy array reduction.
1. `ring.py`: implementation of a "token" send around a ring.
1. `run_ring.sh`: Bash script illustrating how to run the program.
1. `ring.pbs`: PBS script to run the ring program as a job.
1. `round_about.py`: another ring type implementation.
1. `exchange.py`: even ranks send, odd ranks receive, and vice versa.
1. `mpi_count.py`: count amino acids in a long sequence, distributing
   the work over processes.
1. `large_dna.txt`: example data file to use with `mpi_count.py`.
1. `mpifitness.py`: application to time various MPI communications.
1. `pi_mpipool.py`: illustration of using `mpi.futures.MPIPoolExecutor` to
   compute the value of pi using a quadrature method.
1. `run_pi_mpipool.sh`: Bash script to run `pi_mpipool.py`.
1. `file_trafficker.py`: file write/read test application that can run
   serially, multi-threaded, multi-process and MPI.
1. `mpi_io.py`: timing of MPI-IO operations.
1. `translate_bin.py`: translate binary to ASCII data.

## How to run?

The MPIPoolExecutor applications can be run using the command below for MPICH2:
```bash
$ mpiexec -n 1 -usize 3 ./file_trafficker.py --mode mpi ...
```

For Intel MPI/Open MPI:
```bash
$ mpiexec -n 3 python -m mpi4py.futures ./file_trafficker.py --mode mpi ...
```

This would run the application with 2 worker processes.
