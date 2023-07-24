#!/bin/bash
#SBATCH -p postproc*# cluster
#SBATCH --ntasks=3 
#SBATCH --cpus-per-task=1
#SBATCH --time=0-01:00:00
cd /mnt/permanent/hydro/src/CREST_3.0
srun -n3 -N1 -o /mnt/training/crest/qing/CREST_tutorial/demo_project/%j.out -l --multi-prog  /mnt/training/crest/qing/CREST_tutorial/demo_project/demo.conf
