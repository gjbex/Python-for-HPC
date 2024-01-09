import cython


def squares(n: cython.int):
    sqrs: list = []
    i: cython.int = 0
    while i < n:
        sqrs.append(i**2)
        incr(cython.address(i))
    return sqrs

@cython.cfunc
def incr(i: cython.p_int):
    i[0] += 1
