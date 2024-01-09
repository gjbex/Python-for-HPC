import cython
import sys

def primes(nr_primes: cython.int):
    primes: cython.int[1000]
    if nr_primes > 1000:
        nr_primes = 1000
    if not cython.compiled:
        primes = [0] * 1000
        print('fall back on Python', file=sys.stderr)
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
    return [prime for prime in primes[:nr_found]]
