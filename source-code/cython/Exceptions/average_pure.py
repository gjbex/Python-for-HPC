import cython


def average(data, m=0, n=None):
    if n is None:
        n = len(data)
    return _average(memoryview(data), m, n)

def average_no_except(data, m=0, n=None):
    if n is None:
        n = len(data)
    return _average_no_except(memoryview(data), m, n)

@cython.cfunc
@cython.exceptval(-1.0, check=True)
def _average(data, m: cython.int=0, n: cython.int=-1) -> cython.double:
    i: cython.int
    mean: cython.double = 0.0
    for i in range(m, n):
        mean += data[i]
    return mean/(n - m + 1)

@cython.cfunc
def _average_no_except(data, m: cython.int=0, n: cython.int=-1) -> cython.double:
    i: cython.int
    mean: cython.double = 0.0
    for i in range(m, n):
        mean += data[i]
    return mean/(n - m + 1)
