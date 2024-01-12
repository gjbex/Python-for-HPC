VERSION =  $(shell python3-config --extension-suffix)
CYTHON_LIB = pointers_cython.$(VERSION).so
PURE_LIB = pointers_pure.$(VERSION).so

all: $(CYTHON_LIB) $(PURE_LIB)

$(CYTHON_LIB): pointers_cython.pyx
	python setup.py build_ext --inplace

$(PURE_LIB): pointers_pure.py
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) pointers_cython.c pointers_pure.c $(CYTHON_LIB) $(PURE_LIB)
	$(RM) -r build
