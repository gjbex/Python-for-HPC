#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['point_cython.pyx', 'point_pure.py'],
                          language_level='3str')
)
