VERSION = cpython-311-x86_64-linux-gnu
POINTS_LIB = points.$(VERSION).so
POINTS_PURE_LIB = points_pure.$(VERSION).so

all: $(POINTS_LIB)

$(POINTS_LIB): points.pyx points_pure.py
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) points.c points_pure.c $(POINTS_LIB) $(POINTS_PURE_LIB)
