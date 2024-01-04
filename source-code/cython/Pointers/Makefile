VERSION =  cpython-311-x86_64-linux-gnu
CYTHON_LIB = pointers_cython.$(VERSION).so

all: $(CYTHON_LIB)

$(CYTHON_LIB): pointers_cython.pyx
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) pointers_cython.c $(CYTHON_LIB)
