CXX = g++
CXXFLAGS = -O3 -Wall
CPPFLAGS = $(shell python -m pybind11 --includes)
LDFLAGS = -shared -fPIC

EXTENSION_SUFFIX = $(shell python3-config --extension-suffix)
COMPUTATION_LIB = computations$(EXTENSION_SUFFIX)

COMPUTATION_LIB: computations.cpp computations.h computations_bind.cpp
	$(CXX) $(CXXFLAGS) $(CPPFLAGS) $(LDFLAGS) -o $(COMPUTATION_LIB) computations.cpp computations_bind.cpp

clean:
	$(RM) $(COMPUTATION_LIB)
