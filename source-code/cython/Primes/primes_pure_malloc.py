import cython
from cython.cimports.libc.stdlib import malloc, free

def primes(nr_primes: cython.int):
    nr_bytes: cython.int = nr_primes*cython.sizeof(cython.int)
    primes: cython.p_int = cython.cast(
                cython.p_int,
                malloc(nr_bytes)
            )
    n: cython.int = 2
    nr_found: cython.int = 0
    while nr_found < nr_primes:
        for prime in primes[:nr_found]:
            if n % prime == 0:
                break
        else:
            primes[nr_found] = n
            nr_found += 1
        n += 1
    result = [prime for prime in primes[:nr_found]]
    free(primes)
    return result
