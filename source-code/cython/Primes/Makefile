VERSION = $(shell python3-config --extension-suffix)
SRC_FILES = primes_cython.pyx \
			primes_malloc.pyx \
			primes_pure_python.py \
			primes_pure_malloc.py
PRIMES_LIBS = $(addsuffix $(VERSION), $(basename $(SRC_FILES)))
C_FILES = $(addsuffix .c, $(basename $(SRC_FILES)))

all: $(PRIMES_LIBS)

%$(VERSION): %.pyx
	python setup.py build_ext --inplace

%$(VERSION): %.py
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) $(PRIMES_LIBS)
	$(RM) $(C_FILES)
	$(RM) -r build/
