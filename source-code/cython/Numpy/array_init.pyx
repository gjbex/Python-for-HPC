import numpy as np


def cons(dims):
    array = np.empty(np.prod(dims))
    _cons(memoryview(array))
    return array.reshape(dims)

cdef void _cons(mv):
    cdef int i
    for i in range(mv.nbytes//mv.itemsize):
        mv[i] = <double> i
