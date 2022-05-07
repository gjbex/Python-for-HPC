CXX=g++
CXXFLAGS=-O3 -std=c++17 -Wall -Wextra -Wpedantic

all: cellular_automaton.exe

cellular_automaton.exe: automaton_runner.o main.o
	g++ $(CXXFLAGS) -o $@ $^

clean:
	$(RM) $(wildcard *.o) $(wildcard *.exe)
	$(RM) core
