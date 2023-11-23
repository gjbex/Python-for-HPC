from cython cimport boundscheck, wraparound


def array_sum(a):
    return _array_sum(memoryview(a.reshape((-1, ))))


cdef double _array_sum(double[:] mem_view):
    cdef double total = 0.0
    cdef m = mem_view.shape[0]
    cdef int i
    with boundscheck(False), wraparound(False):
        for i in range(m):
            total += mem_view[i]
    return total
