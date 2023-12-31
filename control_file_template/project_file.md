## .project
<pre>
################################################################################
# CREST Project File
################################################################################
#Version	=	3.0
# Operation System###############################################################
OS              =       "linux"
###############################################################################
## MODEL Run Time Information
################################################################################
#1. Model Time follows the center based convetion,
# i.e., the time marker the center of the time step.
# For example, the start date is 2001123121 and the timeStep is 6h, 
# which means the accumulation of the first iteration starts at 2001 Dec.,31,18:00 and ends at 2002 Jan. 01, 00:00
# The same convention applies to all model output variables
TimeMarkLS	=	h	#y(year);m(month);d(day);h(hour);u(minute);s(second), Forcing must be converted to mm/TimeMark
#2. All date time of all model variables/files must be defined in the same time zone. UTC is suggested because it is the default for most forcing data
TimeFormatLS	=	yyyymmddHHMM
TimeStepLS	=	1
StartDateLS	=	198701100030
WarmupDateLS	=	198701100130
EndDateLS	= 	198701202330
# Time line of Routing Process######################
LoadDates	=	#
TimeMarkRoute	=	h
TimeFormatRoute	=	yyyymmddHHMM
TimeStepRoute	=	1
StartDateRoute	=	198701100030
WarmupDateRoute	=	198701100130
EndDateRoute	=	198701202330
###############################################################################
# MODEL Options
###############################################################################
RunStyle	=	simu    # simu, cali_SCEUA
TaskType	=	ImportForc # ImportForc,LandSurf,Mosaic,Routing
Feedback	=	No 	# routing feeds the LSM back
hasRiverInterflow	=	No #No: all interflow turns to surface flow in the river
EventMode	=	None	# AnnualPeak|AllEvents|None
###############################################################################
# MODEL Directories
###############################################################################
BasicFormat	=	.tif #any gdal supported formats
UseExtGeographic=	No    # use external geographic files 
BasicPathExt	=	""  # directory of external geographic files
DEMExt		=	""       # external DEM file name
FDRExt		=	""  # external FDR file name
FACExt		=	""  # external FAC file name
streamExt	=	""  # external stream file name
BasicPathInt	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/basic/" #"/shared/manoslab/CT_RT_Fore/substations/01/" # directory of the internal geographic files
###############################################################################
ParamFile	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/param/parameters.txt" # Soil and routing parameter file
###############################################################################
StatePath	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/status/" #???? this is a scratch folder
###############################################################################
ICSPath		=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/ICS/"
###############################################################################
ForcingFile	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/ERA5_forcing_control.txt"
###########################################################################
ResultInitLoc	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/Temp/Temp_Land/" # local directory on the compute node to store intermediate files
ResultInit	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/result/result_ImportForc/" # Intermediate results after ImportForc
ResultMosaic	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/result/result_Mosaic/"# Mosaic land surface result to the extent of basin
ResultAgger	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/result/result_LandSurf/" #Intermediate results after LandSurf, stored as vectorized data.
ResultVal	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/result/ET_Val/" #ET result storage
ResultEx	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/output/" #model output folder
ResultMasks	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/result/NodeMasks/" #Nodemask for parallelism, intermediate
ResultChkPts    =       "/mnt/training/crest/qing/CREST_tutorial/demo_project/result/CheckPoints/" #land surface checkpoint, intermediate
###############################################################################
CalibFormat	=	.txt
CalibPath	=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/calibration/"
CalibMode	=	Parallel # Sequential
###############################################################################
OBSDateFormat	=	yyyymmddHHMM
OBSPath		=	"/mnt/training/crest/qing/CREST_tutorial/demo_project/outlet_obs/" #????
OBSNoDataValue	=	-9999
###############################################################################
#Outlet Information
###############################################################################
HasOutlet	=	Yes
OutletName	=	Wadi_418
SitesShpFile	=	Wadi_418.shp #file name
DBFEName	=	"#"
###############################################################################
#Grid Outputs
###############################################################################
GOVar_Rain	=	yes
GOVar_Snow      =       no
GOVar_EPot	=	no
GOVar_EAct	=	yes
GOVar_W		=	yes
GOVar_SM	=	yes
GOVar_SWE	=	yes
GOVar_IntRain	=	no
GOVar_IntSnow	=	no
GOVar_R		=	no
GOVar_ExcS	=	yes
GOVar_ExcI	=	yes
GOVar_RS	=	no
GOVar_RI	=	no
GOVar_rainBare  =       yes
GOVar_actTranspir =     no 
###############################################################################
SaveDates	=	"" #
SaveDateFormat		=	"yyyymmddHHMM"
DateOffset		=	000000000000
#########################################################
DecompBeforeSrc	=	"gunzip -c "
DecompBeforeDst =	">"
OS		=	"linux"
</pre>

## Time setting

The time convention for CREST is set to center and can not be changed. Means in hourly simulation, the step one is yyyymmdd0030, and the end step of a given day is yyyymmdd2330.

- WarmupDateLS or WarmupDateRoute

Specify the time period for warm up, let the system state of landsurface reach a stable state. The warmup period wont be used for calibration or compute the performance metric, while the simulation will still go through all time period. If not use warmup, set the warmupdate to one step later than the start date to prevent bug in the routing.

## MODEL Options

- RunStyle

sim stands for simulation, option for all steps; cali_SCEUA means calibration, only available for calibrate the routing parameters.

- Feedback

Feedback now function within the routing part, usally not use.

- EventMode

Running simulation/calibration based on events with starttime and endtime specified in a specify file.

## MODEL Directories

- BasicPathInt

Point to the basic file folder, that is the only parameter if only toporgraphy data from basic is used.

- ParamFile

Point to the param folder.

- StatePath

Specify a folder to store intermedian system state.

- ICSPath

Point to the ICS folder.

- ForcingFile

Point to the forcing_control_file.

- Result*

Specify folder path to store results of each processing steps. ResultEx is the final streamflow output folder.

### Calibration configuration

- CalibPath

Point to the Calibration folder, where stored the calibration configurations.

- Parallel

Parallelize the calibration computation, this tutorial focus on using this on Linux machine.

- OBSPath

Folder path that stored observation, named with the site name specified in outlet.shp

### Outlet Information

- HasOutlet

Yes when doing calibration

- OutletName

The site name that served as the observation reference.

- SitesShpFile

Shapefile path that stored the outlet shpafiles. That file could contains multiple sites, that is why we have additional options to specify the one used for calibration/metrics computation.

### Grid Outputs

Specify which intermedian varaiable should show up in the final result. Prefer to keep as is.
