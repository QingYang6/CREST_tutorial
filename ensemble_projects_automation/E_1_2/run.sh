#!/bin/bash
#SBATCH -p fat# cluster
#SBATCH --ntasks=8 --cpus-per-task=1
#SBATCH --mem=128g
#SBATCH --time=0-02:00:00
#SBATCH --nodelist=ncmcn617  #
module load matlab/2024a
cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_2/forcing
rm -rf com_ImportForc  com_LandSurf  com_Mosaic  com_Routing HU  LAI  longwave  prec  PRES  shortwave  TAIR  WINDU  WINDV
cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_2
rm -rf result
cd /g/model/hydro/model/NCM_Operation_CREST/CREST_3.0
srun -o /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_2/%j.out -l --multi-prog  /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_1_2/run.conf
