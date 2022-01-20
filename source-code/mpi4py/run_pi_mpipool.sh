#!/usr/bin/env bash

mpiexec -n 1 -usize 5 ./pi_mpipool.py --nr_points 1000000 --nr_parts 40
