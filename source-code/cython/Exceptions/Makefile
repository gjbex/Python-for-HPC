VERSION = cpython-311-x86_64-linux-gnu
AVERAGE_LIB = average.$(VERSION).so
AVERAGE_PURE_LIB = average_pure.$(VERSION).so

all: $(AVERAGE_LIB) $(AVERAGE_PURE_LIB)

$(AVERAGE_LIB): average.pyx
	python setup.py build_ext --inplace

$(AVERAGE_PURE_LIB): average_pure.py
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) average.c average_pure.c $(AVERAGE_LIB) $(AVERAGE_PURE_LIB)
	$(RM) -r build
