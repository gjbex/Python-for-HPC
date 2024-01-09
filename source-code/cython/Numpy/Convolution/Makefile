VERSION = cpython-311-x86_64-linux-gnu
CONVOLUTION_LIB = convolution_cython.$(VERSION).so
CONVOLUTION_INDEXED_LIB = convolution_cython_indexed.$(VERSION).so
CONVOLUTION_NO_CHECKS_LIB = convolution_cython_no_checks.$(VERSION).so

all: $(CONVOLUTION_LIB) $(CONVOLUTION_INDEXED_LIB) $(CONVOLUTION_NO_CHECKS_LIB)

$(CONVOLUTION_LIB): convolution.pyx
	python setup.py build_ext --inplace

$(CONVOLUTION_LIB): convolution_indexed.pyx
	python setup.py build_ext --inplace

$(CONVOLUTION_LIB): convolution_no_checks.pyx
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) $(wildcard *.c) $(wildcard *.so)
	$(RM) -r build
