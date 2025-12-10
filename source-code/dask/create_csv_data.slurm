#!/usr/bin/env -S bash -l
#SBATCH --account=lpt2_sysadmin
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --time=02:00:00

source .mamba_init.sh
mamba activate python_for_hpc

DATA_DIR=$VSC_SCRATCH/data/time_series
mkdir -p $DATA_DIR

./create_csv_data.py --files 800 --rows 200000 --cols 100 $DATA_DIR
