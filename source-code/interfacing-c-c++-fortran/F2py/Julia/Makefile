F2PY = f2py3
FFLAGS = -fopenmp -O2 -g
VERSION = cpython-38-x86_64-linux-gnu

all: julia.cpython-38-x86_64-linux-gnu.so

julia.$(VERSION).so: julia_set_mod.f90 julia_set_omp_mod.f90
	$(F2PY) -c -m julia --f90flags="$(FFLAGS)" $^

clean:
	$(RM) $(wildcard *.o) $(wildcard *mod) $(wildcard *.so)
