#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('*.pyx')
)
setup(
    ext_modules=cythonize(['array_init.pyx', 'array_init_pure.py',
                           'array_sum.pyx', 'array_sum_pure.py'],
                          language_level='3str')
)
