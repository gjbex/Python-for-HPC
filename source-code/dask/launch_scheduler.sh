#!/usr/bin/env -S bash -l

source ~/.mamba_init.sh
mamba activate python_for_hpc

nohup dask-scheduler &> "scheduler-${PBS_JOBID}.log" &
