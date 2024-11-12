#!/bin/bash
#SBATCH -p cpu
#SBATCH --ntasks=24
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=16G
source ~/miniconda3/bin/activate hydro

# Run the first Python task
python3 -u /g/model/hydro/hydrowork/CREST_work/dummy_projects/Project_Control/ProWRFandTriggerProj.py \
--FED /g/model/wrf/ensembles/2024-11-11-00/m3/grib2 \
--ROUT /g/model/hydro/hydrowork/CREST_work/dummy_projects/test_ensemble_out \
--FOD /g/model/hydro/hydrowork/CREST_work/dummy_projects/Ensemble_WRF/m3 \
--LoS single

# Wait for the first job to complete before starting the second
wait

cp -f /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/forcing/forcing_WRFevent_raw.txt /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/forcing/forcing_WRFevent.txt
sed -i 's|/ENSEMBLE_PATH|/g/model/hydro/hydrowork/CREST_work/dummy_projects/Ensemble_WRF/m3/2024111100UTC|g' /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/forcing/forcing_WRFevent.txt
sed -i 's|OP_new|OP_ensemble/E_2_1|g' /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/forcing/forcing_WRFevent.txt

cp -f /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/run_raw.project /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/run.project
sed -i 's|SDATE|202411110030|g' /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/run.project
sed -i 's|EDATE|202411141230|g' /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/run.project
sed -i 's|WDATE|202411110130|g' /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/run.project
sed -i 's|WRFM|m3|g' /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/run.project
# Submit the second job script (run_LSRT.sh)
ssh ncmmn1 "sbatch /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/E_2_1/run_LSRT.sh"
