import fnmatch
import glob
import os
import os
import time
import sys
from pathlib import Path
from stat import S_ISREG, ST_CTIME, ST_MODE

import pandas as pd# Import Pandas Library
import numpy as np


rscPath=os.scandir("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/SortSite_Records/*.csv")
list_of_files=glob.glob(os.path.join(rscPath+"/*.csv"))
print(rscPath)
#path1=os.path.abspath()

print("-----------------------------------------------------")
# print(list_of_files)
# entries = Path(rscPath)
# for entry in entries.iterdir():
    # print(entry.name)

# print(list_of_files)
latest_file=min(list_of_files,key=os.path.getctime)
# oldest_file=max(list_of_files,key=os.path.getctime)
# print(latest_file)

pd.set_option('max_columns', 11)  #shows 11 cols

files_sorted_by_date = []

# Path to the file/directory
path = rscPath

# Both the variables would contain time
ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)

# Converting the time in seconds to a timestamp
c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)

# print(
#     f"The file located at the path {path}was created at {c_ti} and was last modified at {m_ti} ")

dateInFiles=""
nameOfFiles=""
newstring = ""
newstring = ""
test_string=""
badChars="SortSite_Records"
# for items in list_of_files:#splitting the date from file

for i in list_of_files:
   newstring= i.find("SortSite")
print(newstring)

# dateInFiles=i[-9:-4]
    # nameOfFiles=items[-24:]

# print(str(items))#this will save each file by its date
#     nameOfFiles=items.split("")

    # print(items)


# Function which returns last word

def lastWord(string):
    # split by space and converting
    # string to list and
    lis = list(string.split(" "))

    # length of list
    # length = len(lis)

    # returning last element in list
    return lis
    # [length - 1]



dateInFiles = ""
nameOfFile = ""
newstring = ""
newstring = ""
for i in list_of_files:  # splitting the date from file
    dateInFiles = i[-9:-4]

    # print("Date in files "+dateInFiles)  # this will save each file by its date

# print(nameOfFile)
# Function which returns last word
