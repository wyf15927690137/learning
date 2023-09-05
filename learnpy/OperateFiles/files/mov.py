# Python program to explain shutil.move() method
	
# importing os module
import os

# importing shutil module
import shutil

# path
path = os.getcwd()

# List files and directories
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'


# Source path
source = os.path.join(path, "folder1")

# Destination path
destination = path

# Move the content of
# source to destination
files = os.listdir(source)

# Check if file already exists
if os.path.isdir(destinationPath+'/'+source):
    print(source, 'exists in the destination path!')
    shutil.rmtree(destinationPath+'/'+source)
     
elif os.path.isfile(destinationPath+'/'+source):
    os.remove(destinationPath+'/'+source)
    print(source, 'deleted in', destination)
 
# Move the content
# source to destination
dest = shutil.move(sourcePath, destinationPath)


for file in files:
    source_file = os.path.join(source, file)
    dest_file = os.path.join(destination, file)
    print(source_file)
    print(dest_file)
    shutil.move(source_file, dest_file, copy_function = shutil.copytree)
