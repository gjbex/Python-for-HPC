#!/usr/bin/env bash

module purge
module load Python/3.7.2-foss-2018a
module load HDF5/1.10.1-foss-2018a-lustre

site_packages='python_lib/lib/python3.7/site-packages/'

mkdir -p "$site_packages"
export PYTHONPATH="$site_packages:$PYTHONPATH"
install_dir="$(pwd)/python_lib"

tar xaf h5py-3.2.1.tar.gz
cd h5py-3.2.1

export CC=mpicc
export HDF5_MPI="ON"
export HDF5_DIR="$EBROOTHDF5"

python setup.py install  --prefix="$install_dir"
