import os
import pathlib
import sys

# get the current file directory
print(os.getcwd())

ret = os.path.abspath("16file.py")
print(ret)

# get the relative path
ret = os.path.relpath(__file__)
print(ret)

file1 = "../learncpp/test01.txt"
f1 = open(file1)
for line in f1:
    print(line)

f1.close()

ScriptPath = os.path.split(os.path.realpath(__file__))[0]
print(f"ScriptPath is :{ScriptPath}")
ScriptPath = pathlib.Path(ScriptPath).as_posix()
print(f"ScriptPath is :{ScriptPath}")


filepath = sys.argv[0]
folderpath = os.path.split(filepath)[0] 
filename = os.path.split(filepath)[1]
print(filepath)
print(folderpath)
print(filename)
# new a txt file
file1 = open("./file1.txt",'w')
# new a folder
os.makedirs("./folder1")