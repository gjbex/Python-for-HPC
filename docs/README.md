Although vanilla Python is fairly slow and hence not a good candidate,
there are several options to significantly increase the efficiency of
Python programs.


## Learning outcomes

When you complete this training you will

  * understand and identify performance bottlenecks of Python;
  * know some libraries that can help improve performance for scientific
    computing such as numpy, numexpr and numba;
  * be able to use Cython to improve your code's performance;
  * be able to wrap C, C++ and Fortran code to use it from Python;
  * understand the opportunities and pitfalls of multi-threaded
    programming with Python;
  * be able to write distributed application using MPI;
  * have an understanding of how frameworks for distributed
    computing such as dask and pyspark work.


## Schedule

Total duration: 8 hours.

  | Subject                                     | Duration |
  |---------------------------------------------|----------|
  | introduction and motivation                 |  5 min.  |
  | performance and profiling                   | 45 min.  |
  | libraries                                   | 10 min.  |
  | Numba                                       | 60 min.  |
  | Cython                                      | 90 min.  |
  | interfacing with C/C++/Fortran              | 30 min.  |
  | multi-threaded programming                  | 60 min.  |
  | MPI                                         | 45 min.  |
  | dask                                        | 45 min.  |
  | pyspark                                     | 45 min.  |
  | wrap up                                     | 15 min.  |


## Training materials

Slides are available in the
 [GitHub repository](https://github.com/gjbex/Python-for-HPC),
as well as example code and hands-on material.


## Software environment

Instructions on [how to create the required software environment](software_stack.md)
are available.


## Target audience

This training is for you if you need to use Python for computationally
intensive scientific computing.


## Prerequisites

You will need experience programming in Python, using numpy, and have a passing
familiarity with C/C++.  This is not a training that starts from scratch.

If you plan to do Python programming in a Linux or HPC environment you should
be familiar with these as well.

More concretely, participants should already be comfortable with the following:

* running Python code in Jupyter or from the command line;
* variables, numbers, strings, booleans, and basic containers such as lists,
  tuples, sets, and dictionaries;
* `if`/`else` statements, `for` loops, comprehensions, and writing functions
  with arguments and return values;
* importing modules and reading short Python scripts without needing every line
  explained;
* solid NumPy basics such as array creation, slicing, reshaping,
  broadcasting, vectorized computations, and reductions;
* basic scientific-computing patterns such as timing code, reasoning about
  array shapes, and understanding why vectorized array code can outperform
  explicit Python loops;
* basic file handling and command-line scripting;
* basic familiarity with Linux or HPC workflows, for example running scripts
  on a remote system, editing files in a shell environment, and understanding
  batch jobs at a high level;
* a rough idea of what C or C++ code looks like, so that interfacing examples
  are not completely unfamiliar.

You do not need prior experience with profiling tools, Numba, Cython,
`mpi4py`, Dask, PySpark, HDF5, SWIG, `ctypes`, `f2py`, or writing extension
modules in C/C++/Fortran. Those are part of the training itself.

### Quick self-assessment

If you can do most of the tasks below without looking up basic Python syntax,
you are likely ready for this training.

* create a NumPy array, reshape or slice it, and compute a reduction such as a
  sum or mean;
* explain at a high level why a vectorized NumPy expression can be faster than
  a Python loop over elements;
* read a short script that times a numerical computation and understand what is
  being measured;
* write a function that processes a NumPy array and returns another array or a
  scalar result;
* run a Python script from the command line with one or two arguments and
  interpret the output;
* read a short traceback or runtime error and identify roughly where the
  problem occurred;
* make a small change to an example script or notebook and run it again;
* read a small piece of C or C++ code and at least recognize concepts such as
  loops, variables, and function calls;
* understand the basic idea of running work on multiple cores or multiple
  processes, even if you have not implemented that yourself.

If several of these items still feel difficult, the training will probably move
too fast. In that case, it is better to first refresh Python and NumPy, and if
necessary take a short introduction to Linux/HPC workflows.

For following along hands-on, you need
* laptop or desktop with internet access.
* a system set up so you can connect to an HPC system, an account on an HPC
  system (e.g., VSC, CECI, ...), compute credits if that is required to run
  jobs on the HPC system if you want to use an HPC system;
* a Python environment that can run Jupyter Lab if you want to use your own system;
* access to Google Colaboratory if you prefer not to install software.


## Level of the Material

For participants who already have solid Python and NumPy experience, the material in this training is approximately

* Introductory: 5 %
* Intermediate: 30 %
* Advanced: 65 %

These percentages describe the level of the HPC and performance-engineering
topics covered in the training, not the required entry level in Python itself.


## Trainer(s)

  * Geert Jan Bex ([geertjan.bex@uhasselt.be](mailto:geertjan.bex@uhasselt.be))
