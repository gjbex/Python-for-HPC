VERSION = $(sheel python3-config --extension-suffix)
HELLO_WORLD_LIB = hello_world.$(VERSION).so

all: $(HELLO_WORLD_LIB)

$(HELLO_WORLD_LIB): hello_world.pyx
	python setup.py build_ext --inplace

clean:
	python setup.py clean
	$(RM)  $(HELLO_WORLD_LIB) hello_world.c
	$(RM) -r build
