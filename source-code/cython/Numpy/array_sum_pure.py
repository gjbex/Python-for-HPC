import cython
import numpy as np

def array_sum(array: np.array) -> np.float64:
    shape = array.shape
    array.reshape((-1, ))
    mv: cython.double[:] = array.reshape((-1, ))
    total: cython.double = 0.0
    with cython.boundscheck(False):
        for i in range(mv.shape[0]):
            total += mv[i]
    return total