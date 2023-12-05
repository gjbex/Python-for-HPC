VERSION = cpython-311-x86_64-linux-gnu
ARRAY_SUM_LIB = array_sum.$(VERSION).so
ARRAY_INIT_LIB = array_init.$(VERSION).so
ARRAY_SUM_PURE_LIB = array_sum_pure.$(VERSION).so
ARRAY_INIT_PURE_LIB = array_init_pure.$(VERSION).so
PROFILE = array_sums_prof.txt
override DIM = 1000
override ITER = 10

all: $(ARRAY_SUM_LIB) $(ARRAY_SUM_PURE_LIB) \
	 $(ARRAY_INIT_LIB) $(ARRAY_INIT_PURE_LIB)

$(ARRAY_SUM_LIB): array_sum.pyx
	python setup.py build_ext --inplace

$(ARRAY_INIT_LIB): array_init.pyx
	python setup.py build_ext --inplace

profile: $(ARRAY_SUM_LIB) compute_sums.py
	python -m cProfile -s time \
	    ./compute_sums.py --n $(DIM) --iter $(ITER) > $(PROFILE)

clean:
	python setup.py clean
	$(RM) $(wildcard *.c) $(wildcard *.so)
