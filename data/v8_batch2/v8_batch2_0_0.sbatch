#!/bin/bash
#SBATCH --job-name=v8_batch2_0_0
#SBATCH -A TG-IBN140002
#SBATCH -t 36:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128
#SBATCH -o ../data/v8_batch2/v8_batch2_0_0.run
#SBATCH -e ../data/v8_batch2/v8_batch2_0_0.err
#SBATCH --mail-user=fernandodasilvaborges@gmail.com
#SBATCH --mail-type=end

#SBATCH --mem=1024G
#SBATCH --export=ALL
#SBATCH --partition=large-shared
source ~/.bashrc
cd /home/fborges/Thalamocortical_model/sim/
mpirun -n 128 nrniv -python -mpi init.py simConfig=../data/v8_batch2/v8_batch2_0_0_cfg.json netParams=../data/v8_batch2/v8_batch2_netParams.py
wait
    