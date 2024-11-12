import os
import sys
import subprocess
from datetime import datetime, timedelta
import time

def check_all_done2a(base_folder, ensembles, sleep_interval=60):
    """
    Checks for the existence of 'DONE2a' in each ensemble's grib2 folder.
    Waits and checks repeatedly until all ensembles have the 'DONE2a' file.
    """
    print("Checking for 'DONE2a' file in each ensemble's grib2 folder...")
    
    while True:
        ready_ensembles = []
        for ensemble in ensembles:
            grib2_folder = os.path.join(base_folder, ensemble, "grib2")
            done2a_file = os.path.join(grib2_folder, "DONE2a")
            
            if os.path.exists(done2a_file):
                ready_ensembles.append(ensemble)
            else:
                print(f"'DONE2a' file not yet ready in {grib2_folder}")
        
        if len(ready_ensembles) == len(ensembles):
            print("All 'DONE2a' files are ready. Proceeding with job submissions.")
            break
        else:
            print(f"{len(ready_ensembles)}/{len(ensembles)} ensembles ready. Rechecking in {sleep_interval} seconds...")
            time.sleep(sleep_interval)

def modify_and_submit(base_folder):
    # Define the ensembles
    ensembles = ["m1", "m2", "m3", "m4", "m5"]

    # Define the root folder containing the project subfolders
    root_folder = "/g/model/hydro/hydrowork/CREST_work/dummy_projects/OP_ensemble"

    # Define the specific project folders manually
    project_folders = [os.path.join(root_folder, folder) for folder in ['E_1_1', 'E_1_2', 'E_2_1', 'E_2_2', 'E_3_1']]
    
    # Check for DONE2a files before starting the loop
    check_all_done2a(base_folder, ensembles)

    for i, project_folder in enumerate(project_folders):
        if i >= len(ensembles):
            break  # Only handle as many folders as there are ensembles

        ensemble = ensembles[i]
        run_script_raw = os.path.join(project_folder, "run_LSRT_En_raw.sh")
        run_script = os.path.join(project_folder, "run_LSRT_En.sh")

        # Check if run_LSRT_En_raw.sh exists in the project folder
        if os.path.exists(run_script_raw):
            # Copy run_LSRT_En_raw.sh to run_LSRT_En.sh
            subprocess.run(["cp", run_script_raw, run_script])

            # Define the full path to the current ensemble's grib2 folder
            grib2_folder = os.path.join(base_folder, ensemble, "grib2")

            # Get the base folder date (YYYYMMDDHH)
            folder_date = os.path.basename(base_folder)  # Extracts "2024-08-01-00"
            datetime_raw = folder_date.replace("-", "")  # Removes hyphens for "2024080100"

            # Define SDATE_RAW and SDATE_WRF
            SDATE_RAW = f"{datetime_raw}30"  # Add 30 minutes to MM
            SDATE_WRF = datetime_raw  # Keep the original datetime without the MM part

            # Calculate WDATE_RAW as SDATE_RAW + 1 hour
            SDATE_raw_dt = datetime.strptime(SDATE_RAW, "%Y%m%d%H%M")
            WDATE_RAW = (SDATE_raw_dt + timedelta(hours=1)).strftime("%Y%m%d%H%M")

            # Calculate EDATE_RAW based on the number of files in the grib2 folder, subtract 2 hours
            try:
                num_files = len([f for f in os.listdir(grib2_folder) if os.path.isfile(os.path.join(grib2_folder, f))])
                if num_files >= 2:
                    EDATE_RAW = (SDATE_raw_dt + timedelta(hours=num_files - 2)).strftime("%Y%m%d%H%M")
                else:
                    print(f"Warning: Not enough files in {grib2_folder} to calculate EDATE_RAW")
                    EDATE_RAW = ""
            except FileNotFoundError:
                print(f"Error: grib2 folder not found: {grib2_folder}")
                continue

            # Echo the calculated WDATE_RAW and EDATE_RAW for verification
            print(f"WDATE_RAW for {ensemble}: {WDATE_RAW}")
            print(f"EDATE_RAW for {ensemble}: {EDATE_RAW}")

            # Modify the run_LSRT_En.sh script
            with open(run_script, 'r') as file:
                script_data = file.read()

            script_data = script_data.replace("ENSEMBLEWRF", os.path.join(base_folder, ensemble))
            script_data = script_data.replace("WRFNUM", ensemble)
            script_data = script_data.replace("SDATE_RAW", SDATE_RAW)
            script_data = script_data.replace("WDATE_RAW", WDATE_RAW)
            script_data = script_data.replace("EDATE_RAW", EDATE_RAW)
            script_data = script_data.replace("SDATE_WRF", SDATE_WRF)

            with open(run_script, 'w') as file:
                file.write(script_data)

            # Submit the sbatch job
            print(f"Submitting job in {project_folder} with ensemble {ensemble}")
            subprocess.run(["sbatch", run_script])

            # Wait for 1 minute before the next submission
            print("Waiting for 1 minute before next submission...")
            time.sleep(120)
        else:
            print(f"run_LSRT_En_raw.sh not found in {project_folder}, skipping...")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -u auto_submit.py /path/to/ensembles/YYYY-MM-DD-HH")
        sys.exit(1)

    base_folder = sys.argv[1]

    if not os.path.exists(base_folder):
        print(f"Error: Base folder {base_folder} does not exist")
        sys.exit(1)

    modify_and_submit(base_folder)
