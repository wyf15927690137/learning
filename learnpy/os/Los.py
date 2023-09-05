import os

currentfile = os.path.realpath(__file__)
currentfile1 = os.path.abspath(__file__)
print(currentfile)
print(currentfile1)
dirname = os.path.dirname(currentfile)
print(dirname)
# get the current dir of a process
currentDic = os.getcwd()
print(currentDic)

pa = "D:\\PersonalLearn\\learning\\learnpy\\xml"
for file in os.listdir(pa):
    filePath = os.path.join(pa,file)
    if os.path.isdir(filePath):
        print("%s is dir" %filePath)
    elif os.path.isfile(filePath):
        print("%s is file" %filePath)
    else:
        print("%s is a special file" %filePath)