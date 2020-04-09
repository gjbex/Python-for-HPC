#!/usr/bin/env bash

if [ $# -ne 3 ]
then
    (>&2 echo '### error: expecting WORK_DIR, SCHEDULER and JOBID as arguments' )
    exit 1
fi

WORK_DIR=$1
if [ ! -d "${WORK_DIR}" ]
 then
    (>&2 echo "### error: WORK_DIR '${WORK_DIR}' does not exist" )
    exit 2
fi
SCHEDULER=$2
JOBID=$3

cd "${WORK_DIR}"

source "conda.sh"
conda activate dask 2> /dev/null
if [ $? -ne 0 ]
then
    (>&2 echo '### error: conda environment not sourced correctly' )
fi

nohup dask-worker "${SCHEDULER}" &> "worker-$(hostname)-${JOBID}.log" &
