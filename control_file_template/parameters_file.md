## ./param/parameters.txt
A typical setting is as follows:
<pre>
################################################################################
# CREST Parameters File Format (v3.0)
#########################################################################################
#########################################################################################
#########################################################################################
## Land Cover Parameters
################################################################################
LCC1UseExt			=			No
LCC1Ext			=			""
LCC1			=			LCC.tif
################################################################################
LCC2UseExt			=			No
LCC2Ext			=			""
LCC2			=			LCC.tif
################################################################################
NClasses			=			15
CoverLib			=			CoverLib.csv
##########################################################################################
##########################################################################################
#########################################################################################
## Soil Parameters
##########################################################################################
# depth of soil layers (m)
###############################################################################
nLayers		=		3 # number of model layers
depth_1		=		0.1
depth_2		=		0.3
depth_3		=		1.5
dp			=			4
SoilThermal			=		VIC_410#	Independent_Balances #VIC_410 #
EvapSurfWater			=			Yes
################################################################################
# saturated soil conductivity (mm/h)
################################################################################
KsatType		=			Distributed #
nLayers_Ksat			=			6
Ksat_depth_1			=			0.05 #(m)
Ksat_1						=		KSAT_sd1.tif
Ksat_depth_2			=			0.1 #(m)
Ksat_2			=			KSAT_sd2.tif
Ksat_depth_3			=			0.15 #(m)
Ksat_3			=			KSAT_sd3.tif
Ksat_depth_4			=			0.30 #(m)
Ksat_4			=			KSAT_sd4.tif
Ksat_depth_5			=			0.40 #(m)
Ksat_5			=			KSAT_sd5.tif
Ksat_depth_6			=			1.00 #(m)
Ksat_6			=			KSAT_sd6.tif
################################################################################
# field capacity (%v)
################################################################################
FCType			=			Distributed #
nLayers_FC		=			6
FC_depth_1			=			0.05 #(m)
FC_1						=		FC_sd1.tif
FC_depth_2			=			0.1 #(m)
FC_2			=			FC_sd2.tif
FC_depth_3			=			0.15 #(m)
FC_3			=			FC_sd3.tif
FC_depth_4			=			0.30 #(m)
FC_4			=			FC_sd4.tif
FC_depth_5			=			0.40 #(m)
FC_5			=			FC_sd5.tif
FC_depth_6			=			1.00 #(m)
FC_6			=			FC_sd6.tif
#################################################################################
# Wilting point soil moisture (%)
#################################################################################	
WwpType			=			Distributed #
nLayers_Wwp		=			6
Wwp_depth_1			=			0.05 #(m)
Wwp_1						=		Wwp_sd1.tif
Wwp_depth_2			=			0.1 #(m)
Wwp_2			=			Wwp_sd2.tif
Wwp_depth_3			=			0.15 #(m)
Wwp_3			=			Wwp_sd3.tif
Wwp_depth_4			=			0.30 #(m)
Wwp_4			=			Wwp_sd4.tif
Wwp_depth_5			=			0.40 #(m)
Wwp_5			=			Wwp_sd5.tif
Wwp_depth_6			=			1.00 #(m)
Wwp_6			=			Wwp_sd6.tif
################################################################################
# Saturated(maximal) soil moisture (%)
################################################################################	
SatType				=		Distributed #
nLayers_Sat			=			6
Sat_depth_1				=			0.05 #(m)
Sat_1			=			SAT_sd1.tif
Sat_depth_2			=			0.1 #(m)
Sat_2			=			SAT_sd2.tif
Sat_depth_3			=			0.15 #(m)
Sat_3			=			SAT_sd3.tif
Sat_depth_4			=			0.30 #(m)
Sat_4			=			SAT_sd4.tif
Sat_depth_5			=			0.40 #(m)
Sat_5			=			SAT_sd5.tif
Sat_depth_6			=			1.00 #(m)
Sat_6			=			SAT_sd6.tif
##################################################################################
# organic matter (%w)
################################################################################
OMType				=		Distributed #	
nLayers_OM			=			6
OM_depth_1			=			0.05 #(m)
OM_1			=			ORCDRC_sd1.tif
OM_depth_2			=			0.1 #(m)
OM_2			=			ORCDRC_sd2.tif
OM_depth_3			=			0.15 #(m)
OM_3			=			ORCDRC_sd3.tif
OM_depth_4			=			0.30 #(m)
OM_4			=			ORCDRC_sd4.tif
OM_depth_5			=			0.40 #(m)
OM_5			=			ORCDRC_sd5.tif
OM_depth_6			=			1.00 #(m)
OM_6			=			ORCDRC_sd6.tif
##################################################################################
# bulk density (kg/m^3)
################################################################################
BDType				=		Distributed #	
nLayers_BD			=			6
BD_depth_1				=			0.05 #(m)
BD_1			=			BLD_sd1.tif
BD_depth_2			=			0.1 #(m)
BD_2			=			BLD_sd2.tif
BD_depth_3			=			0.15 #(m)
BD_3			=			BLD_sd3.tif
BD_depth_4			=			0.30 #(m)
BD_4			=			BLD_sd4.tif
BD_depth_5			=			0.40 #(m)
BD_5			=			BLD_sd5.tif
BD_depth_6			=			1.00 #(m)
BD_6			=			BLD_sd6.tif
###########################################################################################
###########################################################################################
# type 3 parameters: Single-Layer (Uniform/Distributed) parameters that may be calibrated #
###########################################################################################	\
# soil quartz (m)
################################################################################
SoilQuartzType						=			Uniform	
SoilQuartzExt			=			""
SoilQuartzUseExt			=				No
SoilQuartz								=			0.693
##################################################################################
# soil roughness (m)
################################################################################
SoilRghType	=	Uniform	
SoilRghExt	=	""
SoilRghUseExt	=	No
SoilRgh		=	0.01
##############################################################################
# minimal volumetric soil mositure of top layer soil mositure
################################################################################
MvResType	=	Uniform	# 0-1
MvResExt	=	""
MvResUseExt	=	No
MvRes		=	0.05
################################################################################
# infiltration curve paramerter b_infilt
################################################################################
BType	=	Uniform	# 0.1-1.5
BExt	=	""
BUseExt	=	No
B	=	0.25
################################################################################	
IMType	=	Distributed	#
IMUseExt=	No
IMExt	=	""
IM	=	IM.tif
################################################################################
## Snow Pack Parameters
################################################################################
# soil roughness (m)
################################################################################
SnowRghType						=			Uniform	
SnowRghExt			=			""
SnowRghUseExt			=				No
SnowRgh								=			0.03
################################################################################
################################################################################	
## routing parameters
################################################################################	
fExcSType	=	Uniform	#
fExcSExt	=	No
fExcSExt	=	""
fExcS	=	1    
################################################################################
fExcIType	=	Uniform	#
fExcIExt=	No
fExcIExt	=	""
fExcI	=	1   
################################################################################	 
coeMType 	=	Uniform	 #Overland flow speed multiplier
coeMUseExt	=	No
coeMExt		=	""
coeM 		=	111.3237
################################################################################				
expMType	=	Uniform	# 
expMUseExt	=	No
expMExt		=	""
expM		=	0.5467
################################################################################
coeRType	=	Uniform	#
coeRUseExt	=	No
coeRExt		=	""
coeR		=	1.8178
################################################################################	
coeSType	=	Uniform	# 
coeSUseExt	=	No
coeSExt		=	""
coeS		=	0.5842   
################################################################################	
KSType		=	Uniform	#
KSUseExt	=	No
KSExt		=	"" 
KS		=	0.0181
################################################################################	
KIType		=	Uniform	# 
KIUseExt	=	No
KSExt		=	""
KI		=	0.3251
################################################################################
delayType	=		Uniform	# delay in timestep
delayUseExt	=	No
delayExt	=	""
delay		=	747
</pre>

- nLayers

Number of soil layers for simulate soil moisture dynamics. Refer to as upper Soil Layer, intermediate Soil Layer, and Lower Soil Layer.

- SoilThermal

The version of the soil thermal module.

- *Type

Uniform or Distributed. For raster input, use Distributed, empirical parameter use Uniform.

- *Ext

Wheter to use special ext for the input file. Use "" if not.

- *UseExt

Wheter to use ext for specify parameter.

## routing parameters

- fExcS

Multiplier to overland(surface) runoff, excS.

- fExcI

Multiplier to interflow runoff, excI.

- coeM

The overland runoff velocity coefficient.

- expM

The overland flow speed exponent.

- coeR

The multiplier used to convert overland flow to channel flow.

- coeI

The multiplier used to convert overland flow to interflow.

- KS

The overland reservoir discharge coefficient.

- KI

The interflow Reservoir discharge coefficient.

## routing parameter setting when running calibration.

Set all routing parameters to 1 for calibration, as the value range specify in the calibration.txt representing the multiplier for each parameter.