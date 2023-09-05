import os
import shutil

# Providing the folder path
origin = r'D:\Test\1'
target = r'D:\Test\2'

os.makedirs(target)

# Fetching the list of all the files
files = os.listdir(origin)

# Fetching all the files to directory
for file_name in files:
    print(file_name)
    source = os.path.join(origin, file_name)
    dest = os.path.join(target, file_name)
    # copy the source file to the dest file
    shutil.copy(source, dest)
print("Files are copied successfully")

