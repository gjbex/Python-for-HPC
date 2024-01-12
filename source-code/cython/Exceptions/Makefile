VERSION = $(shell python3-config --extension-suffix)
AVERAGE_LIB = average$(VERSION)
AVERAGE_PURE_LIB = average_pure$(VERSION)

all: $(AVERAGE_LIB) $(AVERAGE_PURE_LIB)

$(AVERAGE_LIB): average.pyx
	python setup.py build_ext --inplace

$(AVERAGE_PURE_LIB): average_pure.py
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) average.c average_pure.c $(AVERAGE_LIB) $(AVERAGE_PURE_LIB)
	$(RM) -r build
