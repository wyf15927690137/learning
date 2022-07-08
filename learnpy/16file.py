import os

# get the current file directory
print(os.getcwd())

ret = os.path.abspath("16file.py")
print(ret)

# get the relative path
ret = os.path.relpath("H:/learning")
print(ret)

file1 = "../learncpp/test01.txt"
f1 = open(file1)
for line in f1:
    print(line)

f1.close()
