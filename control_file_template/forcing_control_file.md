## forcing_control.txt
A typical setting is as follows:
<pre>
################################################################################
# CREST Forcing Control File
# Version	=	3.0
###############################################################################
# forcing options
###############################################################################
forceImport	=	No
TAIRType	=	MEAN #MINMAX
MinTRain	=	0
MaxTSnow	=	0
HumidityType	=	RH #SH
WindType	=	UV #Total
ref_Height	=	10 #(m) wind speed reference height
FileDateFormat  =       yyyymmdd # this is a daily file
forcPathLoc	=	"/g/model/hydro/demo/CREST/demo_project/Temp/Temp_forcing/"
Interpolation   =       2   #1=NearestNeighbour, 2=BilinearInterpolation
###############################################################################
## total precipitation (mm/timeMark)
###############################################################################
PrecFormat	=	.tif
PrecDateFormat	=	ERA5_yyyy-mm-dd_HHMMSS
PrecDateConv	=	End
PrecDateInterval=	ERA5_0000-00-00_010000
PrecPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
PrecBand	=	11
Prec_LT		=	1 #kg/m^2/s=mm/hour.
Prec_ULim       =       1e5     # physical upper limit
Prec_LLim       =       0       # physical lower lmit 
PrecPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/prec/prec."
###############################################################################
## shortwave radiation (W/m^2)
###############################################################################
SWFormat	=	.tif
SWDateFormat	=	ERA5_yyyy-mm-dd_HHMMSS
SWDateConv	=	End
SWDateInterval	=	ERA5_0000-00-00_010000
SWPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
SWBand		=	12
SW_LT		=	1
SW_ULim		=	1e10	# physical upper limit
SW_LLim		=	0	# physical lower limit
SWPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/SW/sw."
###############################################################################
## longwave radiation (W/m^2)
###############################################################################
LWFormat	=	.tif
LWDateFormat	=	ERA5_yyyy-mm-dd_HHMMSS
LWDateConv	=	End
LWDateInterval	=	ERA5_0000-00-00_010000
LWPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
LWBand		=	13
LW_LT		=	1
LW_ULim         =       1e10    # physical upper limit
LW_LLim         =       0       # physical lower limit
LWPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/LW/lw."
###############################################################################
## Air Temperature (C)
###############################################################################
TAIRFormat	=	.tif
TAIRDateFormat	=	ERA5_yyyy-mm-dd_HHMMSS
TAIRDateConv	=	End
TAIRDateInterval=	ERA5_0000-00-00_010000
TAIRPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
TAIRBand	=	15
TAIR_LT		=	1
TAIR_ULim       =      100    # physical upper limit
TAIR_LLim       =       -273.15       # physical lower limit
TAIRPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/TAIR/TAIR."
###############################################################################
## Humidity SH(kg/kg), RH(%)
###############################################################################
HUFormat	=	.tif
HUDateFormat	=	ERA5_yyyy-mm-dd_HHMMSS
HUDateConv	=	End
HUDateInterval	=	ERA5_0000-00-00_010000
HUPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
HUBand		=	14
HU_LT		=	1
HU_ULim         =       1    # physical upper limit
HU_LLim         =       0       # physical lower limit
HUPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/HU/HU."
###############################################################################
## Pressure (Pa)
###############################################################################
PRESFormat	=	.tif
PRESDateFormat	=	ERA5_yyyy-mm-dd_HHMMSS
PRESDateConv	=	End
PRESDateInterval=	ERA5_0000-00-00_010000
PRESPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
PRESBand	=	7
PRES_LT		=	1
PRES_ULim	=       2e6    # physical upper limit
PRES_LLim	=       0      # physical lower lmit
PRESPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/PRES/PRES."
###############################################################################
## Wind (m/s)
###############################################################################
WIND_UFormat	=	.tif
WIND_UDateFormat=	ERA5_yyyy-mm-dd_HHMMSS
WIND_UDateConv	=	End
WIND_UDateInterval=	ERA5_0000-00-00_010000
WIND_UPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
WIND_UBand	=	1
WIND_U_LT	=	1
WIND_U_ULim     =       200    # physical upper limit
WIND_U_LLim	=       -200       # physical lower limit
WIND_UPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/Wind_U/wind_u."
###############################################################################
WIND_VFormat	=	.tif
WIND_VDateFormat=	ERA5_yyyy-mm-dd_HHMMSS
WIND_VDateConv	=	End
WIND_VDateInterval=	ERA5_0000-00-00_010000
WIND_VPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
WIND_VBand	=	2
WIND_V_LT	=	1
WIND_V_ULim     =	200    # physical upper limit
WIND_V_LLim     =       -200   # physical lower limit
WIND_VPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/Wind_V/wind_v."
###############################################################################
LAIFormat	=	.tif
LAIDateFormat	=	ERA5_yyyy-mm-dd_HHMMSS
LAIDateConv	=	End
LAIDateInterval	=	ERA5_0000-00-00_010000
LAIPathExt	=	"/g/model/hydro/demo/CREST/demo_project/ERA5_forcing/"
LAIBand		=	16
LAI_LT		=	1 
LAI_ULim	=       20    # physical upper limit
LAI_LLim	=       0     # physical lower limit
LAIPathInt	=	"/g/model/hydro/demo/CREST/demo_project/forcing/LAI/lai."
</pre>

- *DateConv

Date convention, specify the time range representation for each forcing variable. In the case of ERA5, it should be End.

- *DateFormat

Format of the main string body of the specify forcing file, should correspond to the DateInterval.

- *DateInterval

The instance of one time step correspond to DateFormat, also should consist with timestep setting in the .project file.

- *Format

Ext of the input forcing file. Use the final Ext if multiple '.' contains in the file name.

- *PathExt

Path to the specify forcing variable files, including any prefix strings before the patter of LAIDateInterval.

- *Band

Band number of the anticipated forcing variable, from the file.

- *_LT

Multiplier, use when unit adjustment is needed.

- *_ULim, *LLim

Upper limit and lower limit of the vairable values, in case of outlier.

- *PathInt

Path and prefix strings to store the imported forcing variable, default format is .mat.

