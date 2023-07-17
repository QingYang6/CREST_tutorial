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
StartDateLS	=	201508010030
WarmupDateLS	=	201508010130
EndDateLS	= 	201508310030
# Time line of Routing Process######################
LoadDates	=	#
TimeMarkRoute	=	h
TimeFormatRoute	=	yyyymmddHHMM
TimeStepRoute	=	1
StartDateRoute	=	201508010030
WarmupDateRoute	=	201508010130
EndDateRoute	=	201508310030
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
BasicPathInt	=	"/g/model/hydro/demo/CREST/demo_project/basic/" #"/shared/manoslab/CT_RT_Fore/substations/01/" # directory of the internal geographic files
###############################################################################
ParamFile	=	"/g/model/hydro/demo/CREST/demo_project/param/Parameters_hourly_naugatuck_opt.txt" # Soil and routing parameter file
###############################################################################
StatePath	=	"/g/model/hydro/demo/CREST/demo_project/status/" #???? this is a scratch folder
###############################################################################
ICSPath		=	"/g/model/hydro/demo/CREST/demo_project/ICS/"
###############################################################################
ForcingFile	=	"/g/model/hydro/demo/CREST/demo_project/NLDAS_forcing_control.txt"
###########################################################################
ResultInitLoc	=	"/g/model/hydro/demo/CREST/demo_project/Temp/Temp_Land/" # local directory on the compute node to store intermediate files
ResultInit	=	"/g/model/hydro/demo/CREST/demo_project/result/result_init/" # inter intermediate result this is a scratch folder
ResultMosaic	=	"/g/model/hydro/demo/CREST/demo_project/result/Mosaic/"# Mosaic land surface result to the extent of basin
ResultAgger	=	"/g/model/hydro/demo/CREST/demo_project/result/result_hourly/" #land surface result
ResultVal	=	"/g/model/hydro/demo/CREST/demo_project/result/ET_Val/" #ET result storage
ResultEx	=	"/g/model/hydro/demo/CREST/demo_project/output/" #model output folder
ResultMasks	=	"/g/model/hydro/demo/CREST/demo_project/result/NodeMasks/" #Nodemask for parallelism, intermediate
ResultChkPts    =       "/g/model/hydro/demo/CREST/demo_project/result/CheckPoints/" #land surface checkpoint, intermediate
###############################################################################
CalibFormat	=	.txt
CalibPath	=	"/g/model/hydro/demo/CREST/demo_project/calibration/"
CalibMode	=	Parallel # Sequential
###############################################################################
OBSDateFormat	=	yyyymmddHHMM
OBSPath		=	"/g/model/hydro/demo/CREST/demo_project/outlet_obs/" #????
OBSNoDataValue	=	-9999
###############################################################################
#Outlet Information
###############################################################################
HasOutlet	=	No
OutletName	=	0128500
SitesShpFile	=	Naugatuck_01208500.shp #file name
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
<pre>