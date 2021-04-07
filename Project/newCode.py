import fnmatch
import glob
import os
import shutil
from datetime import datetime, time, timezone
import pandas as pd  # Import Pandas Library
import numpy as np
import pytz
#getting the values form latest and oldest files
# rscPath="C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/"
# list_of_files=glob.glob(os.path.join(rscPath+'/*.csv'))
# print("-----------------------------------------------------")
# latest_file=min(list_of_files,key=os.path.getctime)
# oldest_file=max(list_of_files,key=os.path.getctime)
# print(latest_file)
pd.set_option('max_columns', 11)  #shows 11 cols
# Read CSV Files into Data Frames
input1 = pd.read_csv("/Resources/SortSite Scan_AMIS_v2.7.1_03.22.csv")
input2 = pd.read_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/SortSite_Records/SortSite Scan_FYPS_v7.0_3.22.csv")
# input1=pd.read_csv(oldest_file)
# input2=pd.read_csv(latest_file)
input1 = pd.DataFrame(input1)#converting each input into DF
idx = 0
input1['Source'] = 1  #setting this value, means comming from input 1
input2 = pd.DataFrame(input2)
input2['Source'] = 2  #comming from input 2
allDF = pd.concat([input1, input2])#concatinating both df into one
allDF['Index'] = np.arange(allDF.shape[0])#setting new index
print(allDF)
uniqueValues = allDF.drop_duplicates(#droping duplicates
    subset=["Category", "Guidelines", "Priority", "Count", "Line", "Description", "Detail", "Help", "URL", "Target URL",
            "Reference"], keep=False)
#setting up the values for each column
uniqueValues['Status'] = ""
date_fixed="04/01/2021"
date_found="03/01/2021"
allDF['Status'] = ""
today=datetime.now()
month_First=today.replace(day=1,hour=0,minute=0,second=0,microsecond=0)#setting the datefound to first of each month
# uniqueValues.set_option('mode.chained_assignment',None)
print(allDF)
for row in uniqueValues.iterrows():#iterating through each row
    source = row[1]["Source"]
    index = row[1]["Index"]
    if source==1:#setting conditions
        allDF.loc[(allDF.Index)==index, "Status"]="New"
        allDF.loc[(allDF.Index)==index, "Date_Found"]=date_found
    if source==2:
        allDF.loc[(allDF.Index)==index, "Status"]="Fixed"
        allDF.loc[(allDF.Index)==index, "Date_Fixed"]=date_fixed
allDF.loc[(allDF.Status)=='', "Status"]="Open"
allDF.loc[(allDF.Date_Fixed).isnull(), "Date_Fixed"] = "N/A"#if values are NaN assign it to N/A
allDF.loc[(allDF.Date_Found).isnull(), "Date_Found"] = "N/A"
# FinalResult=allDF.drop_duplicates(#droping duplicates from both files just printing one from each
#     subset=["Category", "Guidelines", "Priority", "Count", "Line", "Description", "Detail", "Help", "URL", "Target URL",
#             "Reference","Status","Date_Found","Date_Fixed"])
# print(FinalResult)
# print(FinalResult.to_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/Files_Scanned/newestRecord.csv"))
#     print(i+",")#printing all the files available in NIH folder
#
# my_dic={key:i for i, key in enumerate(all_files)}
# print(my_dic)
    # if i.__contains__("AMIS"):
    #     input11+=i
    #     print("Coming from if statement "+input11[3,5])
# modTime=os.path.getmtime(latest_file)
# modidtime=datetime.utcfromtimestamp(modTime).strftime('%y-%m-%d %H:%M:%S')
#
# print(modidtime)