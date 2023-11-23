import cython
import numpy as np

def cons(dims: tuple[int]) -> np.array:
    array = np.empty(np.prod(dims))
    mv: cython.double[:] = array
    for i in range(mv.nbytes//mv.itemsize):
        array[i] = np.float64(i)
    return array.reshape(dims)