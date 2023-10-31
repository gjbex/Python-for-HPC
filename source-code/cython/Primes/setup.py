#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['primes_cython.pyx', 'primes_pure_python.py'],
                          language_level='3str')
)
