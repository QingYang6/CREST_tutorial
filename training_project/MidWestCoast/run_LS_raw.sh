#!/bin/bash
#SBATCH -p matlab # cluster
#SBATCH --tasks=3 --cpus-per-task=1
#SBATCH --mem=48g
#SBATCH --time=0-04:00:00
#SBATCH --nodelist=ncmcn620

# Clean-up the directories
cd PROJECT_PATH/forcing
rm -rf com_ImportForc com_LandSurf com_Mosaic com_Routing

# Change to the model directory
cd /g/model/hydro/model/NCM_Operation_CREST/CREST_3.0

# Run the first task (run.conf)
srun -o PROJECT_PATH/%j_LandSurface.out -l --multi-prog PROJECT_PATH/LandSurface.conf
