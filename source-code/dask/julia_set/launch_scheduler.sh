#!/usr/bin/env bash

source "conda.sh"
conda activate dask 2> /dev/null
if [ $? -ne 0 ]
then
    (>&2 echo '### error: conda environment not sourced correctly' )
fi

nohup dask-scheduler &> "scheduler-${PBS_JOBID}.log" &
