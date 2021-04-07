import fnmatch
import glob
import os
from stat import S_ISREG, ST_MTIME, ST_MODE
from datetime import datetime, time, timezone
from pathlib import Path

import os, sys, time
import shutil
from stat import S_ISREG, ST_MTIME, ST_MODE
from datetime import datetime, time, timezone
from pathlib import Path
from collections import defaultdict
import pandas as pd  # Import Pandas Library
import numpy as np
from docutils.utils.math.math2html import file

basepth="C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources"
NIHReportspth=basepth+"/NIH_Reports/"
CopyOFRecords=basepth+"/CopyOfRecords"
SortSiteRpth=basepth+"/SortSite_Records"
FilesScnpth=basepth+"/Files_Scanned"
FinalListOfScans=pd.read_csv(basepth+"/Files_Scanned/FinalListOfScans.csv")
FinalListOfScansdf=pd.DataFrame(FinalListOfScans)
FinalListOfScansdf=pd.DataFrame(columns=['Name','Version','Date'])


nameasList=[]
allName=[]
entriesSSR=Path(SortSiteRpth)
for entry in entriesSSR.iterdir():#iterating over the directory SSR
      #getting the name of each file on folder
    # print(entry.name)
   #  print(entry.absolute())
    values=entry.name.split("_")
    # print(values)
    name = values[1]
    version=values[2]
    date=values[3][:-4]
    nameasList.append(entry.name)
    allName.append([name,version,date])



allNamepd=pd.DataFrame(columns=['Name','Version','Date'])
allNamepd=allNamepd.append(pd.DataFrame(allName, columns=['Name', 'Version', "Date"]),
                                                 ignore_index=True)
# print(FinalListOfScans)
filesMerged=pd.concat([allNamepd, FinalListOfScansdf])
uniquepd=filesMerged.drop_duplicates(subset=['Name','Version','Date'],keep=False)

uniquepd.sort_values(by='Date', ascending=False)#need to find a way to check the versions oldest to newest
uniquepd.sort_values(by='Name', ascending=False)#oldest to newest
# print(uniquepd)

allnames=""
allversion=""
alldates=""

for (columnName, columnData) in uniquepd.iteritems():
    for names in columnData:
        allnames=names #getting all the names in uniquepd
        print(allnames)
        # print('Column Name : ', columnName)
    break
    # print('Column Contents : ', columnData.values)

for entry in NIHReportspth:
        print(entry)





      # input2FilePath = scan #may need to add rest of path depending on how file is actually formatted
      # for file in NIHReportFolderThing:
      #     appNameNIH = file.split("_")
      #     input1FilePath = file #again path may need to be added
      #     if appNameNIH== appNameScan:
      #        run script using input1FilePath and input2File path this is where functions are helpful!
      #

