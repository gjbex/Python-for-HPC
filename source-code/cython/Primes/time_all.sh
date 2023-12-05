#!/usr/bin/env bash

hyperfine --parameter-list mode python,cython,pure_python "./primes.py --n 1000 {mode} > /dev/null"
