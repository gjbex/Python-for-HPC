#!/usr/bin/env -S bash -l
#SBATCH --account=lpt2_sysadmin
#SBATCH --cluster=wice
#SBATCH --time=00:10:00
#SBATCH --ntasks=1 --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH hetjob
#SBATCH --ntasks=4 --cpus-per-task=8

# file name to store scheduler information for workers and client
scheduler_file="$(pwd)/scheduler_${SLURM_JOB_ID}.json"

# activate environment that has dask installed
mamba activate python_for_hpc

# launch dask server process
echo "launching dask-server"
srun --exclusive \
     --het-group=0 \
    --ntasks=$SLURM_NTASKS_HET_GROUP_0 \
    --cpus-per-task=$SLURM_CPUS_PER_TASK_HET_GROUP_0 \
    --mem=$SLURM_MEM_PER_NODE_PACK_GROUP_0 \
    dask scheduler --scheduler-file $scheduler_file &

# give server time to start
sleep 5

# launch dask worker processes
for i in $(seq $SLURM_NTASKS_HET_GROUP_1)
do
    echo "launching dask-worker $i"
    srun --exclusive \
        --het-group=1 \
        --ntasks=1 \
        --cpus-per-task=$SLURM_CPUS_PER_TASK_HET_GROUP_1 \
        --mem=$SLURM_MEM_PER_NODE_PACK_GROUP_1 \
        dask worker --scheduler-file $scheduler_file &
done

# give workers time to start
sleep 20

# start the client process
python dask_distr_test.py \
    --scheduler-file $scheduler_file \
    --verbose
