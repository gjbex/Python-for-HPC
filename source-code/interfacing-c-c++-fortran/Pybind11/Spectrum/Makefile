CXX = g++
CXXFLAGS = -std=c++17 -g -O2 -Wall -Wextra -Wpedantic
CPPFLAGS = $(shell python3 -m pybind11 --includes)
LDFLAGS = -fPIC -shared 
LDLIBS = -lm

PYBIND_SUFFIX = $(shell python3-config --extension-suffix)

bindings: spectrum.cpp
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) $(LDFLAGS) -o spectrum$(PYBIND_SUFFIX) $^

clean:
	$(RM) $(wildcard *.so) $(wildcard *.o)
	$(RM) core $(wildcard core.*)
