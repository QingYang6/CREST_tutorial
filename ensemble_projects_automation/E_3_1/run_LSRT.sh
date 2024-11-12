#!/bin/bash
#SBATCH -p matlab # cluster
#SBATCH --ntasks=7 --cpus-per-task=1
#SBATCH --mem=110g
#SBATCH --time=0-05:30:00
#SBATCH --nodelist=ncmcn619

module load matlab/2024a

# Clean-up the directories
cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_3_1/forcing
rm -rf com_ImportForc  com_LandSurf  com_Mosaic  com_Routing HU  LAI  longwave  prec  PRES  shortwave  TAIR  WINDU  WINDV
cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_3_1
rm -rf result status Temp

# Change to the model directory
cd /g/model/hydro/model/NCM_Operation_CREST/CREST_3.0

# Run the first task (run.conf)
srun -o /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_3_1/%j_run.out -l --multi-prog /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_3_1/run.conf

# Run the second task (routing.conf) with only one task
srun --ntasks=1 -o /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_3_1/%j_routing.out -l --multi-prog /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_3_1/routing.conf

cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_3_1/forcing
rm -rf com_ImportForc  com_LandSurf  com_Mosaic  com_Routing HU  LAI  longwave  prec  PRES  shortwave  TAIR  WINDU  WINDV
cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_3_1
rm -rf result status Temp
