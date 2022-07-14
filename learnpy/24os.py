import os
import os.path
import sys
import copy

if  os.path.isdir("C:\\Users\\yanfeiw\\wyf_workspace"):
    os.system("echo %PATH%")
else:
    print("yes")

print(sys.argv)
args = copy.deepcopy(sys.argv)
print(args)