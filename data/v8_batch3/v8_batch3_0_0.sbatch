#!/bin/bash
#SBATCH --job-name=v8_batch3_0_0
#SBATCH -A TG-IBN140002
#SBATCH -t 22:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128
#SBATCH -o ../data/v8_batch3/v8_batch3_0_0.run
#SBATCH -e ../data/v8_batch3/v8_batch3_0_0.err
#SBATCH --mail-user=fernandodasilvaborges@gmail.com
#SBATCH --mail-type=end

#SBATCH --mem=1024G
#SBATCH --export=ALL
#SBATCH --partition=large-shared
source ~/.bashrc
cd /home/fborges/Thalamocortical_model/sim/
mpirun -n 256 nrniv -python -mpi init.py simConfig=../data/v8_batch3/v8_batch3_0_0_cfg.json netParams=../data/v8_batch3/v8_batch3_netParams.py
wait
    