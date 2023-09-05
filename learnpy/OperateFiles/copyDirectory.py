import os
import shutil

# Providing the folder path
origin = r'D:\Test\1'
target = r'D:\Test\2'

# target folder don't exsit, will rename the source folder to target
shutil.copytree(origin, target)
print("Files are copied successfully")
