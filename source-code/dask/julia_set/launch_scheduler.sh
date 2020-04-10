#!/usr/bin/env bash

source "conda.sh"
conda activate python_for_hpc 2> /dev/null
if [ $? -ne 0 ]
then
    (>&2 echo '### error: conda environment not sourced correctly' )
fi

nohup dask-scheduler &> "scheduler-${PBS_JOBID}.log" &
