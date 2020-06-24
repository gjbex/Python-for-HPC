# Software stack

This training requires a non-trivial software stack so using the conda package
manager will simplify your life considerably.


## git version control

The repository for this training session is available on Github, and cloning this
repository on you own machine will give you access to all training material.

If you don't have a git client installed, consult the following [web page on how to
install](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) one on
your platform of choice.


## Python & conda

The most convenient way to install the required software is using the conda
environment manager.  conda is available on Linux, MacOS and Windows.  You can use
conda from the command line when you install miniconda which is available for
[download](https://docs.conda.io/en/latest/miniconda.html).  The website provides
installation instructions for each platform.

Remember to install miniconda on a file system with enough free space since conda
environments quickly take multiple gigabytes of disk space.

Alternatively, you can install Anaconda, a GUI application to manage Python
environments.  For Windows, this may be the most convenient option.  Anaconda is
available for Windows, MacOS and Linux and can be downloaded from the
[Anaconda website](https://www.anaconda.com/products/individual).


## Training environment

To create and use the conda environment for this training, open a terminal window and
follow the steps below.

1. Clone the Github repository:
   ```bash
   $ git clone git@github.com:gjbex/Python-for-HPC.git
   ```
2. Change into the newly created directory:
   ```bash
   $ cd Python-for-HPC
   ```
1. Create the conda environment for this training session:
   ```bash
   $ conda env create -f environment.yml
   ```
1. Activate the environment:
   ```bash
   $ conda activate python_for_hpc
   ```

Now you can run Python scripts in this terminal, or start a Jupyter notebook.
