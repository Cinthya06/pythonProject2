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



basepth="C:/Users/cinthyavelaochaga/PycharmProjects/pythonProject/Resources"
NIHReportspth=basepth+"/NIH_Reports/"
CopyOFRecords=basepth+"/CopyOfRecords"
SortSiteRpth=basepth+"/SortSite_Records"
FilesScnpth=basepth+"/Files_Scanned"
FinalListOfScans=pd.read_csv(basepth+"/Files_Scanned/FinalListOfScans.csv")
FinalListOfScanspd=pd.DataFrame(FinalListOfScans)
FinalListOfScanspd=pd.DataFrame(columns=['Name','Version','Date'])





nameasList=[]
allNames=[]
ssrvlas=[]
list_ofFiName=[]
list_files=[]
entriesSSR=Path(SortSiteRpth)
for entry in entriesSSR.iterdir():#iterating over the directory SSr
    values=entry.name.split("_")
    input2=""
    absvals2=entry.absolute()
    input2=pd.read_csv(absvals2)#will loop throuh each file
    # putting all values in FinalListOfScan whatever is set as input2
    absolutevals=input2

    namessr = values[1] #getting all name files
    # print(namessr) #is printing all name of files under ssr

    versionssr=values[2]
    datessr=values[3][:-4]
    list_ofFiName.append(entry.name)
    list_files.append([namessr, versionssr, datessr])  # check name and the version if read , we dont read it or add it to lis tof files
    # print(list_files)


    allNamepd = pd.DataFrame(columns=['Name', 'Version', 'Date'])
    allNamepd = allNamepd.append(pd.DataFrame(list_files, columns=['Name', 'Version', 'Date']),
                                  ignore_index=True)
# print(allNamepd)
#     FinalListOfScans.drop(FinalListOfScans.filter(regex="Unname"),axis=1, inplace=True)
# print(FinalListOfScans)
    filesMerged = pd.concat([allNamepd, FinalListOfScans])
# print(filesMerged)
    uniquepd = filesMerged.drop_duplicates(subset=['Name', 'Version', 'Date'], keep=False)
# print(uniquepd)
    listOfNamesonuniquepd = []
    uniquepdNames = ""
    for rows in uniquepd.iterrows():  # will get all the vals from unique ps from col 'Name'
        updnames = uniquepd['Name']
        updversion = uniquepd['Version']
        upddate = uniquepd['Date']

        for i in updnames:
            uniquepdNames = i
            # print(uniquepdNames)
            entriesNIH = Path(NIHReportspth)
            for entry in entriesNIH.iterdir():  # iterating through NIH list of files
                namenih = entry.name  # first will be amis
                nihabspath = entry.absolute()
                if uniquepdNames == namenih:
                    abspath1 = nihabspath
                # print("setting this as base path for input1")
                # print(abspath1)
                input1 = pd.read_csv(abspath1)
                input2=absolutevals
                #Adding the existing code

                input1 = pd.DataFrame(input1)  # converting each input into DF
                input1['Source'] = 1  # setting this value, means comming from input 1
                input2 = pd.DataFrame(input2)
                input2['Source'] = 2  # comming from input 2
                allDF = pd.concat([input1, input2])  # concatinating both df into one
                allDF['Index'] = np.arange(allDF.shape[0])  # setting new index
                uniqueValues = allDF.drop_duplicates(  # droping duplicates
                subset=["Category", "Guidelines", "Priority", "Count", "Line", "Description", "Detail", "Help", "URL",
                "Target URL",
                "Reference"], keep=False)
                         # setting up the values for each column
                #         # uniqueValues.insert(13, "Status", "")
                date_fixed = ""
                allDF['Status'] = ""
                today = datetime.today().strftime('%m.%d')
                for row in uniqueValues.iterrows():  # iterating through each row
                    source = row[1]["Source"]
                    index = row[1]["Index"]
                    if source == 1:  # setting conditions
                        allDF.loc[(allDF.Index) == index, "Status"] = "Fixed"
                        allDF.loc[(allDF.Index) == index, "Date_Found"] = "N/A"
                        allDF.loc[(allDF.Index) == index, "Date_Fixed"] = today
                    if source == 2:
                        allDF.loc[(allDF.Index) == index, "Status"] = "New"
                        allDF.loc[(allDF.Index) == index, "Date_Fixed"] = "N/A"
                        allDF.loc[(allDF.Index) == index, "Date_Found"] = today

                        allDF.loc[(allDF.Status) == '', "Status"] = "Open"
                        allDF.loc[(allDF.Date_Fixed).isnull(), "Date_Fixed"] = "N/A"  # if values are NaN assign it to N/A
                        allDF.loc[(allDF.Date_Found).isnull(), "Date_Found"] = "N/A"

                        FinalResult = allDF.drop_duplicates(  # droping duplicates from both files just printing one from each
                            subset=["Category", "Guidelines", "Priority", "Count", "Line", "Description", "Detail", "Help", "URL",
                                    "Target URL",
                                    "Reference", "Status", "Date_Found", "Date_Fixed"])

                print(FinalResult)
                # print(FinalResult.to_csv(NIHReportspth+namenih))
                #



            else:
                # print("")
                # print("Just adding files to NIH and setting values as open")
                input2 = pd.DataFrame(input2)
                input2['Status'] = "Open"
                input2['Date_Found'] = datessr
                input2['Date_Fixed'] = "N/A"

                # print(input2.to_csv(NIHReportspth + uniquepdNames))

        # columnSeries=uniquepd[column]
        # namesinUnipd=columnSeries.values
        break

# print(listofUnique)

# for files in listofUnique:
#     print(files)

# # # setting name version date from input2
# FinalListOfScans=pd.DataFrame([[namessr,versionssr,datessr]],columns=['Name','Version','Date'])
# print(FinalListOfScans)#printing the name of Files on List


# entriesNIH = Path(NIHReportspth)
# for entry in entriesNIH.iterdir():
#     namenih=entry.name #first will be amis
#     nihabspath=entry.absolute()
#     if uniquepdNames == namenih:
#             abspath1=nihabspath
#             print("setting this as base path for input1")
#             print(abspath1)
#             input1=pd.read_csv(abspath1)
#             # print("Comparing Files with same name")
#     else:print("")
#     # print("Just adding files to NIH and setting values as open")
# input2=pd.DataFrame(input2)
# input2['Status'] ="Open"
# input2['Date_Found']=date
# input2['Date_Fixed']="N/A"

# print(input2.to_csv(NIHReportspth+uniquepdNames))
# #
#     #
#     #
#































# ssrdir=os. listdir(SortSiteRpth)
# nihpth= os. listdir(NIHReportspth)
# allName1=[]
# # if len(nihpth )== 0:
# #     print("Empty Directory in NIH Records")
# for row in uniquepd.iterrows():
#         # print(row)
#
#         nameupd = uniquepd['Name'].values[0]
        # print(nameupd)
        # versionupd=uniquepd['Version'].values[1]
        # dateupd=uniquepd['Date'].values[2]
        # allName1.append([nameupd,versionupd,dateupd])

        # entriesssr=os.listdir(SortSiteRpth)
        # entriesNIH = os.listdir(NIHReportspth) #will give me list of files in the directory
        # for entries in entriesssr:
            # if nameupd  in entries:
                # print(entries)

        # setVals =FinalListOfScanspd.append(allName1) #seeting the values from each iteration to Final List of Scans
        # setVals.drop(columns=['Name','Version','Date'],inplace=True)
        # setVals.rename(columns={0: "Name",1:"Version",2:"Date"},
        #           inplace=True)
        # FinalListOfScans=setVals
        # print(FinalListOfScans)

        # if nameupd in entriesNIH:
           # filedf=whatever ps we have to assing




        # if nameupd not in entriesNIH:
         # print("Name not found :"+nameupd)

    # print("Creating one file: ")

        # filedf=pd.DataFrame()
        # # print(filedf.to_csv(NIHReportspth+nameupd)) #creating a file + name
        #
        # break



#setting the values to the new files under NIH
# todayDate = datetime.today().strftime('%m.%d')
# uniquepd.insert(3, "Status", "Open")
# uniquepd.insert(4, "Date_Found", todayDate)#from the file
# uniquepd.insert(5, "Date_Fixed", "")


















# if len(nihpth) ==1:
# input1=""
#
#
#     else:
#         file_list=[]  #from merged list split name, version, date
#         ssrentryArr = []







# mergedList=uniquepd.values.tolist() #converting merged values to list


# for row in uniquepd.iterrows():


# d=defaultdict(list)
# for row in mergedList:#getting all the records grouped by name
#     d[row[0]].append(row)
# print(d["AMIS"])


# values=mergedList[0]
#
# aux=1
# while aux <= len(mergedList):#working code
#     if values[0] in mergedList[aux][0]:
#         # print("getting the 2 match files ")
#         # print(values[0],values[1])#process when I have 2 files with the same name
#         # print(mergedList[aux][0],mergedList[aux][1])#getting the versions
#         destdir = SortSiteRpth
#         # get all entries in the directory w/ stats
#         entries = (os.path.join(destdir, fn) for fn in os.listdir(destdir))
#         entries = ((os.stat(path), path) for path in entries)
#         entriesSSR = Path(SortSiteRpth)
#         # print(entriesSSR)
#         # leave only regular files, insert creation date
#         entries = ((stat[ST_MTIME], path)
#                    for stat, path in entries if S_ISREG(stat[ST_MODE]))
#
#         for cdate, path in sorted(entries):  # working
#             basePath = os.path.basename(path)  # getting base name
#             fullPath = os.path.abspath(path)
#
#             if (values[0] and mergedList[aux][0]) in fullPath:#want to make a acondition to get both files
#                 path1 = ""
#                 path2 = ""
#                 # print(fullPath)
#
#
#
#
#         break
#
# else:

# print(uniquepd)

# print("No other file to compare")
  #no coincidences unique files nothing to compare
# aux+=1






# for i in range(len(mergedList)):
#         for j in range(len(mergedList[i])):# if j=="AMIS":# print(mergedList[i][j])

# lisofvalues=['Name','Version','Date']
# zipobj=zip(mergedList,lisofvalues)
# dicofwords=dict(zipobj)
# print(dicofwords)

# ssrdir=os. listdir(SortSiteRpth)
# directory= os. listdir(NIHReportspth)
# if len(directory )== 0:
#     print("Empty Directory in NIH Records")
#     if len(ssrdir) == 0:
#          print(("No Records Found"))
#     else:
#         file_list=[]  #from merged list split name, version, date
#         ssrentryArr = []
#
 # going over the ssr dir and converting the files in array
     
        # ssrentryArr = [f for f in entriesSSR.iterdir() if os.path.isfile(f)]
        # print(ssrentryArr)#getting all values from SSR path
        # for i in ssrentryArr:
            # fname = i[0]
            # fversion = i[1]
            # fdate = i[2]
            # print[i]



                
                











          
          









































