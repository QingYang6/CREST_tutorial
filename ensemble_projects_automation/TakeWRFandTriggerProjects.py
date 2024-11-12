from datetime import datetime,timedelta
import os,glob,re,argparse,time,shutil,rasterio,multiprocessing
import pandas as pd
from osgeo import gdal,osr
import numpy as np
from functools import partial

class Timer(object):
    def __init__(self, name=None):
        self.name = name
    def __enter__(self):
        self.tstart = time.time()
    def __exit__(self, type, value, traceback):
        if self.name:
            print('[%s]' % self.name,)
        print('Elapsed: %s' % (time.time() - self.tstart))

def GetGeoInfo(FileName,band):
    SourceDS = gdal.Open(FileName)
    NDV = SourceDS.GetRasterBand(band).GetNoDataValue()
    xsize = SourceDS.RasterXSize
    ysize = SourceDS.RasterYSize
    GeoT = SourceDS.GetGeoTransform()
    Projection = osr.SpatialReference()
    Projection.ImportFromWkt(SourceDS.GetProjectionRef())
    DataType = SourceDS.GetRasterBand(band).DataType
    return NDV, xsize, ysize, GeoT, Projection, DataType

def CreateGeoTiff(NewFileName, Array, driver, NDV,
                  xsize, ysize, GeoT, Projection, DataType):
    # Set nans to the original No Data Value
    if NDV is not None:
        Array[np.isnan(Array)] = NDV
    # Set up the dataset
    DataSet = driver.Create(NewFileName, xsize, ysize, 1, DataType, options=['COMPRESS=DEFLATE'])
    # the '1' is for band 1.
    DataSet.SetGeoTransform(GeoT)
    DataSet.SetProjection(Projection.ExportToWkt())
    # Write the array
    DataSet.GetRasterBand(1).WriteArray(Array)
    if NDV is not None:
        DataSet.GetRasterBand(1).SetNoDataValue(NDV)
    return NewFileName

def listdirs(rootdir):
    listdirs=[]
    listname=[]
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            listdirs.append(d)
            listname.append(file)
    return listdirs, listname

def replacestr(file_prj,newfile,text_to_search,replacement_text):
    with open(file_prj, 'r') as file:
        data = file.read()
    for itxt in range(len(text_to_search)):
        data = data.replace(text_to_search[itxt], replacement_text[itxt])
    with open(newfile, 'w') as file:
        file.write(data)
    print("Text replaced "+ newfile)

def WRF_bandselect(list_rawWRF,outdir,idx):
    trawWRF = list_rawWRF[idx]
    src = rasterio.open(trawWRF)
    out_img = os.path.join(outdir,os.path.split(trawWRF)[1])
    CREST_requiredWRF = {'Pressure [Pa]':{'GRIB_ELEMENT': 'PRES','GRIB_SHORT_NAME': '0-SFC'},
    'Temperature [C]':{'GRIB_ELEMENT': 'TMP','GRIB_SHORT_NAME': '2-HTGL'},
    'Relative humidity [%]':{'GRIB_ELEMENT': 'RH','GRIB_SHORT_NAME': '2-HTGL'},
    'u-component of wind [m/s]':{'GRIB_ELEMENT': 'UGRD','GRIB_SHORT_NAME': '10-HTGL'},
    'v-component of wind [m/s]':{'GRIB_ELEMENT': 'VGRD','GRIB_SHORT_NAME': '10-HTGL'},
    'hr Total precipitation [kg/(m^2)]':{'GRIB_ELEMENT': 'APCP','GRIB_SHORT_NAME': '0-SFC'},
    'Downward short-wave radiation flux [W/(m^2)]':{'GRIB_ELEMENT': 'DSWRF','GRIB_SHORT_NAME': '0-SFC'},
    'Downward long-wave radiation flux [W/(m^2)]':{'GRIB_ELEMENT': 'DLWRF','GRIB_SHORT_NAME': '0-SFC'},
    'Upward short-wave radiation flux [W/(m^2)]':{'GRIB_ELEMENT': 'USWRF','GRIB_SHORT_NAME': '0-SFC'},
    'Upward long-wave radiation flux [W/(m^2)]':{'GRIB_ELEMENT': 'ULWRF','GRIB_SHORT_NAME': '0-SFC'}}
    index_bandWRF = []
    for iCWr in CREST_requiredWRF:
        for isrc in range(1,src.count+1):
            if iCWr in src.tags(isrc)['GRIB_COMMENT'] and \
                CREST_requiredWRF[iCWr]['GRIB_ELEMENT'] in src.tags(isrc)['GRIB_ELEMENT'] \
                and src.tags(isrc)['GRIB_SHORT_NAME'] == CREST_requiredWRF[iCWr]['GRIB_SHORT_NAME']:
                index_bandWRF.append(isrc)
    #for i in List_tagsCREST:
    #    index_bandWRF.append([idx for idx, s in enumerate(List_tagsWRF) if i in s][0])
    out_meta = src.meta.copy()
    out_meta.update({"count": len(index_bandWRF)})
    with rasterio.open(out_img, 'w', **out_meta) as dest:
        for band_nr, iband in enumerate(index_bandWRF, start=1):
            dest.write(src.read(iband), band_nr)

def mapworker(inlist,outdir,task='bandselct',tDT=None,toutdir_pre=None):
    #print('Use '+str(multiprocessing.cpu_count())+' CPUs')
    #print('Use '+str(concurrent.futures.ThreadPoolExecutor()._max_workers)+' Threads')
    idx_all = range(len(inlist))
    #args = ((inlist, outdir, idx) for idx in idx_all)
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #        executor.map(WRF_bandselect,args)
    if task == 'bandselct':
        func = partial(WRF_bandselect, inlist, outdir)
        with multiprocessing.Pool(24) as p:
            p.map(func,idx_all)
    else:
        func = partial(WRF_toPrecandForcing, inlist, outdir,tDT,toutdir_pre)
        with multiprocessing.Pool(24) as p:
            p.map(func,idx_all)

def WRF_toPrecandForcing(list_forcnames,toutdir,tDT,toutdir_pre,idx):
    driver = gdal.GetDriverByName('GTiff')
    ifi = list_forcnames[idx]
    tFT = tDT + timedelta(hours=idx)
    lsT = tFT - timedelta(hours=1)
    new_forcpath = os.path.join(toutdir,'WRF_'+tFT.strftime("%Y%m%d%H")+'.tm00')
    shutil.copy(ifi,new_forcpath)
    thisforcfile = new_forcpath
    thisPrecfile = os.path.join(toutdir_pre,'WRF_'+tFT.strftime("%Y%m%d%H")+'.tif')
    if idx >0:
            lastforcfile = list_forcnames[idx-1]
            ds_ts = gdal.Open(thisforcfile)
            ds_ls = gdal.Open(lastforcfile)
            ts_array_pre = ds_ts.GetRasterBand(6).ReadAsArray()
            ls_array_pre = ds_ls.GetRasterBand(6).ReadAsArray()
            ts_array_pre = ts_array_pre - ls_array_pre
            ts_array_pre[ts_array_pre<0]=0
            NDV, xsize, ysize, T_GeoT, Projection, DataType = GetGeoInfo(thisforcfile,6)
            CreateGeoTiff(thisPrecfile, ts_array_pre, driver, NDV,
                        xsize, ysize, T_GeoT, Projection, DataType)
            ds_ts = None
            ds_ls = None
    else:
        ds_ts = gdal.Open(thisforcfile)
        ts_array_pre = ds_ts.GetRasterBand(6).ReadAsArray()
        NDV, xsize, ysize, T_GeoT, Projection, DataType = GetGeoInfo(thisforcfile,6)
        CreateGeoTiff(thisPrecfile, ts_array_pre, driver, NDV,
                        xsize, ysize, T_GeoT, Projection, DataType)
        ds_ts = None

def loopworker(inlist,outdir):
    for i in range(len(inlist)):
        WRF_bandselect(inlist,outdir,i)

def resasmblingWRF(indir,outdir,tDT):
    list_forcnames = glob.glob(os.path.join(indir,'*d02.tm00'))
    list_forcnames.sort(key=os.path.getmtime)
    outeventdir = os.path.join(outdir, tDT.strftime("%Y%m%d%H")+'UTC')
    toutdir_bandselect = os.path.join(outeventdir,'bandselect')
    toutdir = os.path.join(outeventdir,'Forcing')
    toutdir_pre = os.path.join(outeventdir,'Precip')
    os.makedirs(outeventdir, exist_ok=True)
    os.makedirs(toutdir_bandselect, exist_ok=True)
    os.makedirs(toutdir, exist_ok=True)
    os.makedirs(toutdir_pre, exist_ok=True)
    with Timer('WRF band selection '+ toutdir_bandselect):
        mapworker(list_forcnames,toutdir_bandselect)
    list_bsforname = [os.path.join(toutdir_bandselect,os.path.split(ifn)[1]) for ifn in list_forcnames]
    staendDT=[tDT,tDT + timedelta(hours=len(list_bsforname)-1)]
    stDd = {'dtstart': [staendDT[0].strftime("%Y%m%d%H")], 'dtend': [staendDT[1].strftime("%Y%m%d%H")]}
    staendDT_df = pd.DataFrame(data=stDd)
    with Timer('WRF2CRESTinput '+ toutdir):
        mapworker(list_bsforname,toutdir,task='WRF2CRESTinput',tDT=tDT,toutdir_pre=toutdir_pre)
    print ("Forcing Preprocess done " + outeventdir)
    return outeventdir,staendDT_df

def directForcingEventLoop(df_forcData,args):
    for idx, iFPath in enumerate(df_forcData.path):
        tDt = df_forcData.datetime[idx]
        '''extract and get the event start end time df'''
        event_Forcdir,staendDT_df = resasmblingWRF(iFPath,args.FOD,tDt)
        staendDT_df.to_csv(args.EC,index=False)
        newshfile = os.path.splitext(args.ESH)[0]
        newshfile = newshfile+'.sh'
        replacestr(args.ESH,newshfile,['EVENTCSV','FORCINGFOLDER','SIMOUTDIR'],[args.EC,event_Forcdir,args.ROUT])
        os.system('bash '+newshfile)
        time.sleep(930)

def historicalforcingevents(args):
    os.makedirs(args.FOD, exist_ok=True)
    List_WRFdir,AllWRFname = listdirs(args.FED)
    if args.DEF:
        _,exitsWRFname = listdirs(args.DEF)
        set_difference = set(AllWRFname) - set(exitsWRFname)
        left_WRFdir = []
        for iWRF in set_difference:
            ind = AllWRFname.index(iWRF)
            left_WRFdir.append(List_WRFdir[ind])
        List_WRFdir=left_WRFdir
    df_forcData = pd.DataFrame(List_WRFdir, columns=['path'])
    df_forcData['datetime']=pd.to_datetime(df_forcData['path'],format='%Y%m%d%H',exact=False)
    df_forcData = df_forcData.sort_values(by='datetime').reset_index(drop=True)
    print(df_forcData)
    return df_forcData

def singleEventForcsing(args):
    os.makedirs(args.FOD, exist_ok=True)
    df_forcData = pd.DataFrame([args.FED], columns=['path'])
    df_forcData['datetime']=pd.to_datetime(df_forcData['path'],format='%Y-%m-%d-%H',exact=False)
    event_Forcdir,staendDT_df = resasmblingWRF(args.FED,args.FOD,df_forcData.datetime[0])
    staendDT_df.to_csv(args.EC,index=False)
    newshfile = os.path.splitext(args.ESH)[0]
    newshfile = newshfile+'.sh'
    replacestr(args.ESH,newshfile,['EVENTCSV','FORCINGFOLDER','SIMOUTDIR'],[args.EC,event_Forcdir,args.ROUT])
    os.system('bash '+newshfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--FED', type=str, default='/l/users/platon/WRF1/UPPV4.0.1_d02/postprd/uconn_second_part',
                        help='input WRF foler, single or multiple')
    parser.add_argument('--FOD', type=str, default='/g/model/hydro/hydrowork/CREST_work/Extracted_WRF/historical_events',
                        help='output parsed forcing folder')
    parser.add_argument('--LoS', type=str, default='loop',
                        help='loop the events under FED or single event input')
    parser.add_argument('--EC', type=str, default='/g/model/hydro/hydrowork/CREST_work/dummy_projects/Project_Control/WRFtriggerEvent.csv',
                        help='Event CSV file, input to CGE.sh')
    parser.add_argument('--ESH', type=str, default='/g/model/hydro/hydrowork/CREST_work/dummy_projects/Project_Control/WRFtriggerCEG.raw',
                        help='Event subject .sh raw file')
    parser.add_argument('--DEF', type=str, default='/g/model/hydro/hydrowork/CREST_work/Extracted_WRF/historical_events',
                        help='output parsed forcing checkpiont')
    parser.add_argument('--ROUT', type=str, default='/g/model/hydro/hydrowork/CREST_Output/Events/Historical_Events',
                        help='Event Sim destination')
    args, unparsed = parser.parse_known_args()
    print(args)
    if args.LoS == 'loop':
        df_forcData = historicalforcingevents(args)
        directForcingEventLoop(df_forcData,args)
    else:
        singleEventForcsing(args)
