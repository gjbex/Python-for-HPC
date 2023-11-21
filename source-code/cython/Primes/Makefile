VERSION = cpython-311-x86_64-linux-gnu
PRIMES_LIBS = primes_cython.$(VERSION).so primes_cython3.$(VERSION).so \
			  primes_pure_python.$(VERSION).so

all: $(PRIMES_LIBS)

$(PRIMES_LIBS): primes_cython.pyx primes_pure_python.py
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) primes_cython.c primes_cython3.c primes_pure_python.c $(PRIMES_LIBS)
	$(RM) -r build/
