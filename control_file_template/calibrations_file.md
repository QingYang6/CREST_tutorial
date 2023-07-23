## ./param/parameters.txt
A typical setting is as follows:
<pre>
###############################################################################
# CREST Calibrations File (version 3.0)
###############################################################################
iseed	=	-3
maxn 	= 	10000
kstop	=	8
pcento	=	0.001
ngs	=	4
###############################################################################
# calibration of the land surface parameters
###############################################################################
nGVar	=	0
###############################################################################
TarVar1		=	ET# sensi_H/netRad ET
ETFormat	=	.tif
ETDateFormatExt	=	yyyy_doy
ETDateConv	=	Begin
ETDateInterval	=	0000_1
ETPathExt	=	"/shared/stormcenter/Shen/data/ET/CONUS/USA_dailyET_"
ETBand		=	1
ETTsScaling	=	1
ETPathInt	=	"/shared/manoslab/CT_West/obs/ET/et."
ETDateFormatInt	=	yyyymmdd
###############################################################################
NCalibStations	=	1
###############################################################################
[Station 1 Begin]
#Varible		Min		Initial		Max
Name_1		=	Wadi-418
coeM_1		=	1		56.5315		150
expM_1		=	0.1		0.5		1
coeR_1		=	0.1		0.5		1
coeS_1		=	0.033		1		3.33
KS_1		=	0.001		0.5		1
KI_1		= 	0.001		0.5		1
delay_1	=	0		1		3
[Station 1 End]
</pre>
    
### till nGVar 

Configuration of the optimization method: SCEUA, not need to change.

### LandSurface calibration

Currently does not have a aotumatic method for landsurface calibration.

### Routing calibration

Min and Max are the expected multiplier range for the corresponding parameters, Initial represent the initial multiplier value. Recommend to set each parameter to 1 in the ./demo_project/param/parameters.txt, so the range setting here will directly correspond the absolute value of each parameters.

For detail interpretation of each parameter, please refer to parameters_file.md or manual.