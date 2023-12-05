#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

extensions=[
    Extension('julia_cython', ['julia_cython.pyx']),
    Extension('julia_cython_omp', ['julia_cython_omp.pyx'],
              extra_compile_args=['-fopenmp'],\
              extra_link_args=['-fopenmp'])
]

for extension in extensions:
    extension.cython_directives = {'language_level': "3"}

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=extensions,
)
