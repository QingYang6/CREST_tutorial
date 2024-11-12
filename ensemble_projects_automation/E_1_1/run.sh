#!/bin/bash
#SBATCH -p matlab# cluster
#SBATCH --ntasks=7 --cpus-per-task=1
#SBATCH --mem=110g
#SBATCH --time=0-05:00:00
#SBATCH --nodelist=ncmcn619
module load matlab/2024a
cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_1/forcing
rm -rf com_ImportForc  com_LandSurf  com_Mosaic  com_Routing HU  LAI  longwave  prec  PRES  shortwave  TAIR  WINDU  WINDV
cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_1
rm -rf result status Temp
cd /g/model/hydro/model/NCM_Operation_CREST/CREST_3.0 
srun -o /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_1/%j.out -l --multi-prog  /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_1/run.conf
srun -o /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_1/%j.out -l --multi-prog  /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_1/routing.conf
