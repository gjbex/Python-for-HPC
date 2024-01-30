VERSION = $(shell python3-config --extension-suffix)
CYTHON_LIB = point_cython.$(VERSION).so
PURE_LIB = point_pure.$(VERSION).so

all: $(CYTHON_LIB) $(PURE_LIB)

$(CYTHON_LIB): point_cython.pyx
	python setup.py build_ext --inplace

$(PURE_LIB): point_pure.py
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) point_cython.c point_pure.c $(CYTHON_LIB) $(PURE_LIB)
	$(RM) -r build
