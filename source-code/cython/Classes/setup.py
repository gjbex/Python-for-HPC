#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('points.pyx', language_level='3str')
)
