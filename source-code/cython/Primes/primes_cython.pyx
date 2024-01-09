def primes(int nr_primes):
    cdef int primes[1000]
    if nr_primes > 1000:
        nr_primes = 1000
    cdef int n = 2
    cdef int nr_found = 0
    while nr_found < nr_primes:
        for prime in primes[:nr_found]:
            if n % prime == 0:
                break
        else:
            primes[nr_found] = n
            nr_found += 1
        n += 1
    return [prime for prime in primes[:nr_found]]
