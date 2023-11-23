VERSION = cpython-311-x86_64-linux-gnu
PRIMES_LIB = primes_cython.$(VERSION).so

all: $(PRIMES_LIB)

$(PRIMES_LIB): points.pyx
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) primes_cython.c $(PRIMES_LIB)
