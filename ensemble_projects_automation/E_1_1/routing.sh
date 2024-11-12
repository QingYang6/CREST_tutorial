#!/bin/bash
#SBATCH -p matlab# cluster
#SBATCH --ntasks=1 --cpus-per-task=1
#SBATCH --mem=64g
#SBATCH --time=0-06:00:00
#SBATCH --nodelist=ncmcn619  #
module load matlab/2024a
sleep 2h
cd /g/model/hydro/model/NCM_Operation_CREST/CREST_3.0
srun -o /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_1/%j.out -l --multi-prog  /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_1/routing.conf
