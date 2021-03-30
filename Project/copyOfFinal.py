import fnmatch
import glob
import os
import shutil
from datetime import datetime, time, timezone
import pandas as pd  # Import Pandas Library
import numpy as np

pd.set_option('max_columns', 11)  #shows 11 cols
# Read CSV Files into Data Frames
input1=pd.read_csv("/Resources/Input11.csv") #files to read
input2=pd.read_csv("/Resources/Input22.csv")

# input1=pd.read_csv(oldest_file)
# input2=pd.read_csv(latest_file)
input1 = pd.DataFrame(input1)#converting each input into DF

input1['Source'] = 1  #setting this value, means comming from input 1
input2 = pd.DataFrame(input2)
input2['Source'] = 2  #comming from input 2
allDF = pd.concat([input1, input2])#concatinating both df into one
allDF['Index'] = np.arange(allDF.shape[0])#setting new index
uniqueValues = allDF.drop_duplicates(#droping duplicates
    subset=["Category", "Guidelines", "Priority", "Count", "Line", "Description", "Detail", "Help", "URL", "Target URL",
            "Reference"], keep=False)
#setting up the values for each column
uniqueValues.insert(13, "Status", "")

date_fixed="04/01/2021"
allDF['Status'] = ""

today=datetime.today().strftime('%m.%d')
date_found=today


for row in uniqueValues.iterrows():#iterating through each row
    source = row[1]["Source"]
    index = row[1]["Index"]
    if source==1:#setting conditions
        allDF.loc[(allDF.Index)==index, "Status"]="Fixed"
        allDF.loc[(allDF.Index)==index, "Date_Found"]="N/A"
        allDF.loc[(allDF.Index)==index, "Date_Fixed"]=today
    if source==2:
        allDF.loc[(allDF.Index)==index, "Status"]="New"
        allDF.loc[(allDF.Index)==index, "Date_Fixed"]="N/A"
        allDF.loc[(allDF.Index)==index, "Date_Found"]=today

allDF.loc[(allDF.Status)=='', "Status"]="Open"
allDF.loc[(allDF.Date_Fixed).isnull(), "Date_Fixed"] = "N/A"#if values are NaN assign it to N/A
allDF.loc[(allDF.Date_Found).isnull(), "Date_Found"] = "N/A"


FinalResult=allDF.drop_duplicates(#droping duplicates from both files just printing one from each
    subset=["Category", "Guidelines", "Priority", "Count", "Line", "Description", "Detail", "Help", "URL", "Target URL",
            "Reference","Status","Date_Found","Date_Fixed"])


print(FinalResult)
# print(FinalResult.to_csv("C:/Users/15712/PycharmProjects/pythonProject1/Resources/SortSite_Records/newRecord.csv"))
