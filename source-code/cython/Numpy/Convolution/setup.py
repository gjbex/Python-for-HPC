#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize
from pathlib import Path
from distutils.extension import Extension

home_dir = str(Path.home())

extensions = [
    Extension(
        "convolution_cython",
        ["convolution.pyx"],
        include_dirs=[f'{home_dir}/mambaforge/envs/python_for_hpc/lib/python3.11/site-packages/numpy/core/include/'],
    ),
    Extension(
        "convolution_cython_indexed",
        ["convolution_indexed.pyx"],
        include_dirs=[f'{home_dir}/mambaforge/envs/python_for_hpc/lib/python3.11/site-packages/numpy/core/include/'],
    ),
    Extension(
        "convolution_cython_no_checks",
        ["convolution_no_checks.pyx"],
        include_dirs=[f'{home_dir}/mambaforge/envs/python_for_hpc/lib/python3.11/site-packages/numpy/core/include/'],
    ),
]

setup(
    ext_modules=cythonize(extensions,
                          language_level='3str')
)
