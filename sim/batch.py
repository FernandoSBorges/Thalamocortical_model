"""
batch.py 

Batch simulation for S1-thalamus model using NetPyNE

Contributors: salvadordura@gmail.com, fernandodasilvaborges@gmail.com
"""
from netpyne.batch import Batch
from netpyne import specs
import numpy as np

# ----------------------------------------------------------------------------------------------
# Custom
# ----------------------------------------------------------------------------------------------
def custom(i):
    params = specs.ODict()

    params[('seeds', 'conn')] = [4321+i]
    params[('seeds', 'loc')] = [4321+i]
   
    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py')

    return b

# ----------------------------------------------------------------------------------------------
# Inhibitory connections
# ----------------------------------------------------------------------------------------------
def inhib():
    params = specs.ODict()
    
    params[('IEGain')] = [0.5, 0.75, 1.0, 1.25, 1.5]
    params[('IIGain')] = [0.5, 0.75, 1.0, 1.25, 1.5]
    params[('seeds', 'conn')] =  [0, 1, 2, 3, 4]
    params[('seeds', 'conn')] =  [0, 1, 2, 3, 4]

    b = Batch(params=params, netParamsFile='netParams.py', cfgFile='cfg.py')

    return b
    
# ----------------------------------------------------------------------------------------------
# Run configurations
# ----------------------------------------------------------------------------------------------
def setRunCfg(b, type='mpi_bulletin'):
    if type=='mpi_bulletin' or type=='mpi':
        b.runCfg = {'type': 'mpi_bulletin', 
            'script': 'init.py', 
            'skip': True}

    elif type=='mpi_direct':
        b.runCfg = {'type': 'mpi_direct',
            'cores': 12,
            'script': 'init.py',
            'mpiCommand': 'mpiexec', # --use-hwthread-cpus
            'skip': True}

    elif type=='mpi_direct2':
        b.runCfg = {'type': 'mpi_direct',
            'mpiCommand': 'mpirun -n 80 ./x86_64/special -mpi -python init.py', 
            'skip': True}
            
    elif type == 'hpc_slurm_Expanse':
        b.runCfg = {'type': 'hpc_slurm',
                    'allocation': 'TG-IBN140002',
                    'partition': 'compute',
                    'walltime': '1:00:00',
                    'nodes': 1,
                    'coresPerNode': 128,
                    'email': 'fernandodasilvaborges@gmail.com',
                    'folder': '/home/fborges/Thalamocortical_model/sim/',
                    'script': 'init.py',
                    'mpiCommand': 'mpirun',
                    'custom': '#SBATCH --mem=249325M\n#SBATCH --export=ALL\n#SBATCH --partition=compute',
                    'skip': True}
                    
# ----------------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------------
if __name__ == '__main__': 

    for i in range(2):

        b = custom(i) #

        b.batchLabel = 'v7_batch'+str(1+i)  
        b.saveFolder = '../data/'+b.batchLabel
        b.method = 'grid'
        setRunCfg(b, 'hpc_slurm_Expanse')
        # setRunCfg(b, 'mpi_direct')
        b.run() # run batch
