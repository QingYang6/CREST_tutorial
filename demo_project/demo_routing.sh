#!/bin/bash
#SBATCH -p postproc# cluster
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0-01:00:00
cd /mnt/permanent/hydro/src/CREST_3.0
matlab -nodisplay -nosplash -r "CREST('/mnt/training/crest/qing/CREST_tutorial/demo_project/demo.project','mean'); exit;"