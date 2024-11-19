#!/bin/bash
#SBATCH -p cpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G

# Check if input argument (input_folder) is provided
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <input_folder>"
    exit 1
fi

# Input WRF folder and current script location
input_folder="$1"
current_folder="$(pwd)"

# Function to calculate SDATE_RAW, WDATE_RAW, and EDATE_RAW
extract_dates() {
    local input_dir="$1"

    # Extract the base time from the folder name
    local folder_time=$(basename "$input_dir" | grep -oP '\d{10}')
    if [[ -z "$folder_time" ]]; then
        echo "Error: Unable to extract folder time from '$input_dir'."
        exit 1
    fi

    # Convert folder_time to datetime
    local datetime=$(date -d "${folder_time:0:8} ${folder_time:8:2}:00" +"%Y-%m-%d %H:%M")

    # Adjust hour to the nearest valid start time (0030 or 1230)
    if (( ${folder_time:8:2} >= 6 && ${folder_time:8:2} < 18 )); then
        # Set to 1230 of the same day
        datetime=$(date -d "$datetime +6 hours" +"%Y-%m-%d 12:30")
    else
        # Set to 0030 of the next day for hours 18 to 23 or 0 to 5
        datetime=$(date -d "$datetime +6 hours +1 day" +"%Y-%m-%d 00:30")
    fi

    # SDATE_RAW
    local sdate_raw=$(date -d "$datetime" +"%Y%m%d%H%M")

    # WDATE_RAW (SDATE_RAW + 1 hour)
    local wdate_raw=$(date -d "$datetime +1 hour" +"%Y%m%d%H%M")

    # Get the last file's timestamp for EDATE_RAW
    local precip_dir="$input_dir/Precip"
    if [[ ! -d "$precip_dir" ]]; then
        echo "Precip directory not found: $precip_dir"
        exit 1
    fi

    # Extract timestamps and determine EDATE_RAW
    local timestamps=($(ls "$precip_dir" | grep -oP 'WRF_\K[0-9]{10}' | sort))
    local edate_raw="${timestamps[-1]}30"

    echo "$sdate_raw" "$wdate_raw" "$edate_raw"
}

# Calculate SDATE_RAW, WDATE_RAW, and EDATE_RAW
read SDATE_RAW WDATE_RAW EDATE_RAW <<< $(extract_dates "$input_folder")

# Prepare forcing_WRFevent.txt
cp -f ./forcing/forcing_WRFevent_raw.txt ./forcing/forcing_WRFevent.txt
sed -i "s|PARSED_WRF_PATH|$input_folder|g" ./forcing/forcing_WRFevent.txt
sed -i "s|PROJECT_PATH|$current_folder|g" ./forcing/forcing_WRFevent.txt

# Prepare run.project
cp -f ./run_raw.project ./run.project
sed -i "s|SDATE|$SDATE_RAW|g" ./run.project
sed -i "s|EDATE|$EDATE_RAW|g" ./run.project
sed -i "s|WDATE|$WDATE_RAW|g" ./run.project
sed -i "s|PROJECT_PATH|$current_folder|g" ./run.project

# Prepare bash script to submit task, LSRT, LS, and RT
cp -f ./run_LSRT_raw.sh ./run_LSRT.sh
sed -i "s|PROJECT_PATH|$current_folder|g" ./run_LSRT.sh

cp -f ./run_LS_raw.sh ./run_LS.sh
sed -i "s|PROJECT_PATH|$current_folder|g" ./run_LS.sh

cp -f ./run_RT_raw.sh ./run_RT.sh
sed -i "s|PROJECT_PATH|$current_folder|g" ./run_RT.sh

# Prepare .conf script for landsurface and routing run
cp -f ./LandSurface_raw.conf ./LandSurface.conf
sed -i "s|PROJECT_PATH|$current_folder|g" ./LandSurface.conf

cp -f ./routing_raw.conf ./routing.conf
sed -i "s|PROJECT_PATH|$current_folder|g" ./routing.conf