#!/bin/bash
#SBATCH -p fat# cluster
#SBATCH --nodelist=ncmfat01
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=32G
#SBATCH --time=0-01:00:00
cd /g/model/hydro/model/src/CREST_3.0
srun -o /g/model/hydro/hydrowork/CREST_work/CREST_Projects/MidWestCoast/%j.out -l --multi-prog  /g/model/hydro/hydrowork/CREST_work/CREST_Projects/MidWestCoast/run.conf
