import fnmatch
import glob
import os
import shutil
from stat import S_ISREG, ST_MTIME, ST_MODE
from datetime import datetime, time, timezone
from pathlib import Path

import os, sys, time
import pandas as pd  # Import Pandas Library
import numpy as np

basepth = "C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources"
NIHReportspth = basepth + "/NIH_Reports"
SortSiteRpth = basepth + "/SortSite_Records"
FilesScnpth = basepth + "/Files_Scanned"
FinalListOfScans = pd.read_csv(basepth + "/Files_Scanned/FinalListOfScans.csv")
FinalListOfScanspd = pd.DataFrame(FinalListOfScans)
FinalListOfScanspd = pd.DataFrame(columns=['Name', 'Version', 'Date'])

destdir=SortSiteRpth
# get all entries in the directory w/ stats
entries = (os.path.join(destdir, fn) for fn in os.listdir(destdir))
entries = ((os.stat(path), path) for path in entries)
entriesSSR = Path(SortSiteRpth)
# print(entriesSSR)
# leave only regular files, insert creation date
entries = ((stat[ST_MTIME], path)
           for stat, path in entries if S_ISREG(stat[ST_MODE]))


def listToString(s):
    # initialize an empty string
    str1 = ""
# traverse in the string
    for ele in s:
        str1 += ele+"_"

        # return string
    return str1[:-1]

paths="SortSite Scan_"
allName=['AMIS', 'v2.7.1', '03.24']
str1 = ""
print(listToString(allName))

for cdate, path  in sorted(entries):#working
    fullDate=time.ctime(cdate)
    basePath=os.path.basename(path)#getting base name
    fullPath=os.path.abspath(path)
    print(fullPath)


    def copyCertainFiles(source_folder, dest_folder, string_to_match, file_type=None):
        # Check all files in source_folder
        for filename in os.listdir(source_folder):
            # Move the file if the filename contains the string to match
            if file_type == None:
                if string_to_match in filename:
                    shutil.copy2(os.path.join(source_folder, filename), dest_folder)

            # Check if the keyword and the file type both match
            elif isinstance(file_type, str):
                if string_to_match in filename and file_type in filename:
                    shutil.move(os.path.join(source_folder, filename), dest_folder)

    # print(fullPath)