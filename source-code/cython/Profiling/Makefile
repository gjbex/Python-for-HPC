VERSION = $(shell python3-config --extension-suffix)

QUAD_LIBS = quad.$(VERSION).so quad_prof.$(VERSION).so \
            quad_prof_indiv.$(VERSION).so

all: $(QUAD_LIBS)

%.$(VERSION).so: %.pyx
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) *.c $(QUAD_LIBS)
