import glob
import os
from datetime import datetime, time, timezone
from pathlib import Path
import pandas as pd# Import Pandas Library
import numpy as np

#getting the values form latest and oldest files
rscPath="C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/SortSite_Records/"
scans=pd.read_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/Files_Scanned/ListOfScans.csv")
input1=pd.read_csv("/Resources/SortSite Scan_FYPS_v7.0_03.22.csv")
input2 = pd.read_csv("/Resources/SortSite Scan_AMIS_v2.7.1_03.22.csv")
list_of_files=glob.glob(os.path.join(rscPath+'/*.csv'))
NIH_Rportpth="C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/NIH_Reports"
print("-----------------------------------------------------")

pd.set_option('max_columns', 11)  #shows 11 cols

#Getting the list of files from SortSite records
list_of_files=glob.glob(os.path.join(rscPath+'/*.csv'))

# print(list_of_files)




#names of all files on folder /SortSite_Records


#Starting func
entries = Path(rscPath)
list_ofFiName=[]
list_files=[]
dirOfCurrentFile=""
for entry in entries.iterdir():#iterating over the directory
    values=entry.name.split("_")
    name = values[1]
    version=values[2]
    date=values[3][:-4]
    list_ofFiName.append(entry.name)
    list_files.append([name,version,date])



entriesOnNiH_Report=Path(NIH_Rportpth)
for entry in entriesOnNiH_Report.iterdir():
    values = entry.name
    name = values[1]
    version=values[2]
    if list_files is not entriesOnNiH_Report:



        print()

#     if list_files is not scans:
#         scans=pd.DataFrame(list_files)
#
# latest_File_Added=max(list_of_files, key=os.path.getctime)

#ending funct


# print("Latest file added: "+latest_File_Added)


# input1 = pd.read_csv(latest_File_Added)
# print(list_ofFiName)
# with os.scandir(rscPath) as it:
#     for entry in it:
#         if entry.is_file():

input1 = pd.DataFrame(input1)#converting each input into DF
idx = 0
input1['Source'] = 1  #setting this value, means comming from input 1
input2 = pd.DataFrame(input2)
input2['Source'] = 2  #comming from input 2
allDF = pd.concat([input1, input2])#concatinating both df into one
allDF['Index'] = np.arange(allDF.shape[0])#setting new index
uniqueValues = allDF.drop_duplicates(#droping duplicates
    subset=["Category", "Guidelines", "Priority", "Count", "Line", "Description", "Detail", "Help", "URL", "Target URL",
            "Reference"], keep=False)


#setting up the values for each column
uniqueValues['Status'] = ""

today=datetime.today().strftime('%m.%d')

allDF['Status'] = ""


#iterating through each row and assigning values
for row in uniqueValues.iterrows():
    source = row[1]["Source"]
    index = row[1]["Index"]
    if source==1:#setting conditions
        allDF.loc[(allDF.Index)==index, "Status"]="Open"
        allDF.loc[(allDF.Index)==index, "Date_Found"]=today  #from the latest file added in this case input2

    if source==2:
        allDF.loc[(allDF.Index)==index, "Status"]="Fixed"
        allDF.loc[(allDF.Index)==index, "Date_Fixed"]=today #todays date


allDF.loc[(allDF.Status)=='', "Status"]="New"

allDF.loc[(allDF.Date_Fixed).isnull(), "Date_Fixed"] = "N/A" #if values are NaN assign it to N/A
allDF.loc[(allDF.Date_Found).isnull(), "Date_Found"] = today


FinalResult=allDF.drop_duplicates(#droping duplicates from both files just printing one from each
    subset=["Category", "Guidelines", "Priority", "Count", "Line", "Description", "Detail", "Help", "URL", "Target URL",
            "Reference","Status","Date_Found","Date_Fixed"])

# print(FinalResult)
# print(FinalResult.to_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/NIH_Reports/SortSite Scan_LatestMergedRecord_v1.0.0_00.00.csv"))





