#!/bin/bash
#SBATCH -p matlab # cluster
#SBATCH --tasks=1 --cpus-per-task=1
#SBATCH --mem=8g
#SBATCH --time=0-02:00:00
#SBATCH --nodelist=ncmcn620

# Clean-up the directories
cd PROJECT_PATH/forcing
rm -rf com_Routing

# Change to the model directory
cd /g/model/hydro/model/NCM_Operation_CREST/CREST_3.0

# Run the second task (routing.conf) with only one task
srun --ntasks=1 -o PROJECT_PATH/%j_routing.out -l --multi-prog PROJECT_PATH/routing.conf
