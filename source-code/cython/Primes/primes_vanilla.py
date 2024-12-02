def primes(nr_primes):
    primes = [0]*1000
    nr_primes = min(nr_primes, 1000)
    n = 2
    nr_found = 0
    while nr_found < nr_primes:
        for prime in primes[:nr_found]:
            if n % prime == 0:
                break
        else:
            primes[nr_found] = n
            nr_found += 1
        n += 1
    return primes[:nr_found]
