VERSION = $(shell python3-config --extension-suffix)
COMPOUNDS_LIB = compounds.$(VERSION).so

all: $(COMPOUNDS_LIB)

$(COMPOUNDS_LIB): compounds.pyx
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM) compounds.c $(COMPOUNDS_LIB)
