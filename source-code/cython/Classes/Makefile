VERSION = cpython-38-x86_64-linux-gnu
PRIMES_LIB = primes_cython.$(VERSION).so

all: $(PRIMES_LIB)

$(PRIMES_LIB): points.pyx
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	rm -f primes_cython.c $(PRIMES_LIB)
