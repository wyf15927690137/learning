import pandas as pd
import os
import sys

data = pd.read_html("http://si-rdtest1:9090/job/CheckBuild/job/PreCheck_main/5834/flowGraphTable/", skiprows=None,flavor='bs4')
print(type(data))
print(len(data))
print(data[0].index)
print(data[0][0])


# file1 = open("./file1",'w')
# print(sys.argv[0])
filepath = sys.argv[0]
folderpath = os.path.split(filepath)[0] 

InitDataFilePath = os.path.join(folderpath,"INIT_5834")
if not os.path.exists(InitDataFilePath):
    InitDataFile = open(InitDataFilePath,'w',encoding='UTF-8')

InitDataFile = open(InitDataFilePath,'w',encoding='UTF-8')
for oneline in data:
    InitDataFile.write(str(oneline))