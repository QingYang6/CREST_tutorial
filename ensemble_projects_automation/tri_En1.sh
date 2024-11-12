#!/bin/bash
#SBATCH -p cpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=16:00:00

# Define paths
ENSEMBLE_DIR="/g/model/wrf/ensembles/"
PYTHON_PATH="/g/home/hydroper/miniconda3/envs/hydro/bin/python"
SCRIPT_PATH="/g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble/auto_submit.py"

# Get current date and format it to YYYY-MM-DD-00
current_date=$(date +"%Y-%m-%d-00")
target_folder_path="${ENSEMBLE_DIR}${current_date}"

# Change to the appropriate directory
cd /g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble

# Run the Python script with the determined folder
$PYTHON_PATH -u $SCRIPT_PATH $target_folder_path
