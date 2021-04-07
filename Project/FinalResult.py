from datetime import datetime
from pathlib import Path

import pandas as pd
import numpy as np
import glob
import os

#getting the list of files under SortSite_Records where all records will be added
rscPath="C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/SortSite_Records/"
list_of_files=glob.glob(os.path.join(rscPath+'/*.csv'))
NIH_Rportpth="C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/NIH_Reports"
#Printing list of files available in sortSite records
listOfFilesScanned=pd.read_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/Files_Scanned/FinalListOfScans.csv")
listOfFilesScannedpd=pd.DataFrame(listOfFilesScanned)
list_of_files=glob.glob(os.path.join(rscPath+'/*.csv'))

# print(list_of_files)

# print("-----------------------------------------------------")
#names of all files on folder /SortSite_Records
entriesSSR = Path(rscPath)

list_ofFiName=[]
list_files=[]
dirOfCurrentFile=""
for entry in entriesSSR.iterdir():#iterating over the directory SSR
      #getting the name of each file on folder
    values=entry.name.split("_")
    name = values[1]
    version=values[2]
    date=values[3][:-4]
    list_ofFiName.append(entry.name)
    list_files.append([name,version,date])#check name and the version if read , we dont read it or add it to lis tof files
print(list_files)
    # if list_files is not listOfFilesScannedpd:
    #     listOfFilesScannedpd=pd.DataFrame(list_files)#adding those values to a list ofFiles scanned
    # if list_files is listOfFilesScannedpd:
    #   continue










#print list of files scanned and not scanned
# latest_File_Added=max(list_of_files, key=os.path.getctime)

#method to iterate over SortSiterecord and check if they are on NIH reports and list of scans
# lisofNIHrepors=[]
# entriesOnNiH_Report=Path(NIH_Rportpth)#nothing for now
# for entry in entriesOnNiH_Report.iterdir():
#     values = entry.name
#     name = values[1]
#     version=values[2]



#method to go over all SSR and check for names and version of files
# for entry in entriesSSR.iterdir():
#     values = entry.name
#     name = values[1]
#     version = values[2]
#     if(name== name) & (version != version):
#         # print(values.name)







#have to sort the values
latestMergedScan=pd.DataFrame()
latestMergedScan= pd.DataFrame(columns=['Name','Version','Date'])#adding columns
latestMergedScan = latestMergedScan.append(pd.DataFrame(list_files, columns=['Name', 'Version',"Date"]), ignore_index=True)
latestMergedScan.sort_values(by='Name')

latestMergedScan.to_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/Files_Scanned/FinalListOfScans.csv")

# print(latestMergedScan)#adding in pd list of all files in Sort_Site records

#if the name is not fourn on nih resports
#allrecords merged
# allMergedRecord=pd.read_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/NIH_Reports/SortSite Scan_LatestMergedRecord_v1.0.0_00.00.csv") #allfiles merged


# pd.set_option('max_columns',11) #will show 11 columns only
# input1=pd.read_csv(latest_File_Added) #latest file added to folder that has not been scanned
# input2=pd.read_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/NIH_Reports/SortSite Scan_LatestMergedRecord_v1.0.0_00.00.csv") #allfiles merged#allfiles merged
#
# #converting inputs in DF
# input1=pd.DataFrame(input1)
# input1['Source']=1
#
# input2=pd.DataFrame(input2)
# input2['Source']=2
#
# # conbinations of 2 inputs in to 1 DF
# allDF=pd.concat([input1, input2])
#
# #setting a new caolumn to index
# allDF['Index']=np.arange(allDF.shape[0])
#
# #dropping the dup from both dfs =allDF
# uniqueValues=allDF.drop_duplicates(
#     subset=["Category","Guidelines","Priority","Count","Line","Description","Detail","Help","URL","Target URL",
#     "Reference"],keep=False)
#
# #setting up the values for each column
# # uniqueValues.insert(13, "Status", "")
# date_Fixed=""
# date_Found=""
#
# # allDF.insert(13,"Status","")
# todayDate=datetime.today().strftime('%m.%d')
#
#
# for row in uniqueValues.iterrows():
#     source=row[1]["Source"]
#     index=row[1]["Index"]
#
#     if source==1:#setting conditions where the file is coming from
#
#         allDF.loc[(allDF.Index)==index, "Status"]="Fixed"
#         allDF.loc[(allDF.Index)==index, "Date_Found"]=date #from files
#         allDF.loc[(allDF.Index)==index, "Date_Fixed"]=todayDate
#     if source==2:
#
#         allDF.loc[(allDF.Index)==index, "Status"]="New"
#         allDF.loc[(allDF.Index)==index, "Date_Fixed"]="N/A"
#
# allDF.loc[(allDF.Status)=='', "Status"]="Open"
# allDF.loc[(allDF.Date_Fixed).isnull(),"Date_Fixed"]="N/A"
# allDF.loc[(allDF.Date_Found).isnull(), "Date_Found"]=todayDate
#
#
# finalDF=allDF.drop_duplicates(#dropping all the dups from all
#     subset=["Category", "Guidelines","Priority","Count","Line","Description","Detail","Help","URL","Target URL",
#            "Reference", "Status","Date_Found" ,"Date_Fixed" ])
#
#
# # print(finalDF)
# print(finalDF.to_csv("C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources/NIH_Reports/SortSite Scan_LatestMergedRecord_v1.0.0_00.00.csv"))