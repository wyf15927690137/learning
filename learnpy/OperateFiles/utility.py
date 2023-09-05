import os
import os.path
import time
import shutil
import platform
import glob
import stat
import zipfile
import subprocess
import tempfile
import sys

# global defines
utilityScriptPath = os.path.split(os.path.realpath(__file__))[0]

# platform checking functions
def isWindows():
	systemString = platform.system();
	if systemString == "Windows":
		return True
	else:
		return False

def isLinux():
	systemString = platform.system();
	if systemString == "Linux":
		return True
	else:
		return False

def createDirectory(destDir):
	if not os.path.isdir(destDir):
		os.mkdir(destDir)
		#print("the destination directory:%s is created." %destDir)
	return
	
def isSameFile(sourceFile, destFile):
	if not os.path.isfile(sourceFile):
		#print("The source file:%s does not exist." %sourceFile)
		return False

	if not os.path.isfile(destFile):
		#print("The destination file:%s does not exist." %destFile)
		return False

	sourceFileName = os.path.basename(sourceFile)
	destFileName =  os.path.basename(destFile)
	if sourceFileName != destFileName:
		return False

	sourceFileMtime = os.path.getmtime(sourceFile)
	destFileMtime = os.path.getmtime(destFile)
	#print("sourceFile:%s Mtime:%s" %(sourceFile, sourceFileMtime))
	#print("destFile:%s Mtime:%s" %(destFile, destFileMtime))
	if destFileMtime != sourceFileMtime:
		return False
	
	return True
	
def removeFile(filePath):
	if not os.path.isfile(filePath):
		#print("The source file:%s does not exist." %filePath)
		return

	os.chmod(filePath, stat.S_IWRITE)
	os.remove(filePath)

	return


def removeReadonly(filePath, fullRight = False):
	#by default set as 0x750
	rwx = (stat.S_IRWXU + stat.S_IRGRP + stat.S_IXGRP) if not fullRight else (stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)
	if os.path.isdir(filePath):
		for root, dirs, files in os.walk(filePath):
			for fileName  in files:
				fullPath = os.path.join(root, fileName)
				if os.path.islink(fullPath):
					linkto = os.readlink(fullPath)
					if os.path.isfile(linkto):
						os.chmod(linkto, rwx)
				else:
					os.chmod(fullPath, rwx)
			for dirName in dirs:
				fullDirPath = os.path.join(root, dirName)
				os.chmod(fullDirPath, rwx)
	else:
		if os.path.islink(filePath):
			linkto = os.readlink(filePath)
			if os.path.isfile(linkto):
				if os.access(linkto, os.W_OK):
					os.chmod(linkto, rwx)
		else:
			os.chmod(filePath, rwx)

	return

def removeDirectory(filePath):
	if not os.path.isdir(filePath):
		#print("The source directory:%s does not exist." %filePath)
		return

	for root, dirs, files in os.walk(filePath):
		for fileName  in files:
			fullPath = os.path.join(root, fileName)
			if os.path.islink(fullPath):
				linkto = os.readlink(fullPath)
				if os.path.isfile(linkto):
					if os.access(linkto, os.W_OK):
						os.chmod(linkto, stat.S_IWRITE)
			else:
				os.chmod(fullPath, stat.S_IWRITE)

	shutil.rmtree(filePath, ignore_errors=True)

	return

def copyFileToDirectory(sourceFile, destDir):
	if not os.path.isdir(destDir) :
		print("the destination directory:%s does not exist." %destDir)
		return

	sourcefiles = glob.glob(sourceFile)
	if len(sourcefiles) == 0:
		print("The file(s) don't exist in the source folder:%s." %sourceFile)
		sys.exit(1)
		return

	for oneSourceFile in sourcefiles:
		if not os.path.isfile(oneSourceFile):
			continue
			
		fileName = os.path.basename(oneSourceFile)
		#print("fileName:%s" %fileName)
		destFile = os.path.join(destDir, fileName)
		#print("destFile:%s" %destFile)

		if os.path.isfile(destFile) :
			if not isSameFile(oneSourceFile, destFile):
				if os.path.islink(oneSourceFile):
					linkto = os.readlink(oneSourceFile)
					if os.path.islink(destFile):
						os.remove(destFile)
					os.symlink(linkto, destFile)
					#print("symlink:%s is updated in the directory:%s" %(fileName, destDir))
				else:
					os.chmod(destFile, stat.S_IRWXU+stat.S_IRWXG+stat.S_IROTH)
					shutil.copy2(oneSourceFile, destDir)
					#print("File:%s is updated in the directory:%s" %(fileName, destDir))
		else:
			if os.path.islink(oneSourceFile):
				linkto = os.readlink(oneSourceFile)
				if os.path.islink(destFile):
					os.remove(destFile)
				os.symlink(linkto, destFile)
				#print("symlink:%s is created in the directory:%s" %(fileName, destDir))
			else:
				shutil.copy2(oneSourceFile, destDir)
				#print("File:%s is created in the directory:%s" %(fileName, destDir))
	return

def copyTreeToDirectory(sourceDir, destDir):
	if not os.path.isdir(sourceDir) :
		print("the source directory:%s does not exist." %sourceDir)
		sys.exit(1)
		return

	if not os.path.isdir(destDir) :
		print("the destination directory:%s does not exist." %destDir)
		return

	subNames = os.listdir(sourceDir)
	for subName in subNames:
		sourceName = os.path.join(sourceDir, subName)
		destName = os.path.join(destDir, subName)

		if os.path.islink(sourceName):
			if not isSameFile(sourceName, destName):
				if os.path.isfile(destName) or os.path.islink(destName):
					os.remove(destName)

				linkto = os.readlink(sourceName)
				os.symlink(linkto, destName)
		elif os.path.isdir(sourceName):
			if not os.path.isdir(destName):
				os.mkdir(destName)
			copyTreeToDirectory(sourceName, destName)
		else:
			if not isSameFile(sourceName, destName):
				# remove readonly
				if os.path.isfile(destName):
					os.chmod(destName, stat.S_IRWXU+stat.S_IRWXG+stat.S_IROTH)
				shutil.copy2(sourceName, destName)
	return

# The input inDir must be a sub valid dir of root dir.
def getRelativeSubDirs(inDir, rootDir):

	subRelativePathes = ""

	if not os.path.isdir(rootDir) :
		print("the start directory:%s does not exist." %rootDir)
		return subRelativePathes

	if not os.path.isdir(inDir) :
		print("the root directory:%s does not exist." %inDir)
		return subRelativePathes

	subRelativePathes += os.path.relpath(inDir, rootDir)
	subRelativePathes += " "

	subNames = os.listdir(inDir)
	for subName in subNames:
		subFullName = os.path.join(inDir, subName)
		if os.path.isdir(subFullName):
			subRelativePathes += getRelativeSubDirs(subFullName, rootDir)

	return subRelativePathes

def zipFolderUnderWindows(parentPath, folder):
	if len(parentPath) == 0:
		print("The parent path cannot be empty.")
		return

	if len(folder) == 0:
		print("The folder name cannot be empty.")
		return

	destDir = os.path.normpath(parentPath);

	zipFileName = folder + ".zip"

	# remove old zip file
	zipFilePath = os.path.join(destDir, zipFileName)
	if os.path.isfile(zipFilePath):
		os.chmod(zipFilePath, stat.S_IWRITE)
		os.remove(zipFilePath)

	# change working directory
	oldCwd = os.getcwd()
	os.chdir(destDir)
	
	# create zip files
	# use 7z tool first
	zipExePath = os.path.join(utilityScriptPath, "tools/Windows/7z.exe")
	if os.path.isfile(zipExePath):
		zipCommand = zipExePath + " a " + zipFileName + " " + folder
		os.system(zipCommand)
	else:
		zf = zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED)
		for dirPath, dirNames, fileNames in os.walk(folder):
			for fileName in fileNames:
				#print(fileName)
				fileFullPath = os.path.join(dirPath, fileName)
				if (os.path.isfile(fileFullPath)):
					zf.write(fileFullPath)
		zf.close()

	# restore working directory
	os.chdir(oldCwd)

	return

def zipFolderUnderLinux(parentPath, folder):
	if len(parentPath) == 0:
		print("The parent path cannot be empty.")
		return

	if len(folder) == 0:
		print("The folder name cannot be empty.")
		return

	destDir = parentPath;

	zipFileName = folder + ".tar.gz"

	# remove old zip file
	zipFilePath = os.path.join(destDir, zipFileName)
	if os.path.isfile(zipFilePath):
		os.remove(zipFilePath)

	# change working directory
	oldCwd = os.getcwd()
	os.chdir(destDir)
	
	# create zip files
	ZipCommand = "tar zcvf " + zipFileName + " ./" + folder + " >/dev/null"
	os.system(ZipCommand)

	# restore working directory
	os.chdir(oldCwd)

	return

def zipFolder(parentPath, folder):
	if isLinux():
		zipFolderUnderLinux(parentPath, folder)
	elif isWindows():
		zipFolderUnderWindows(parentPath, folder)
	return

def unzip2FolderUnderWindows(parentPath, folder):
	if len(parentPath) == 0:
		print("The parent path cannot be empty.")
		return

	if len(folder) == 0:
		print("The folder name cannot be empty.")
		return

	destDir = parentPath

	# check zip file
	zipFileName = folder + ".zip"

	zipFilePath = os.path.join(destDir, zipFileName)
	if not os.path.isfile(zipFilePath):
		print("The zip file:%s does not exist." %zipFilePath)
		return

	# remove old folder
	oldFolder = os.path.join(destDir, folder)
	if os.path.isdir(oldFolder):
		shutil.rmtree(oldFolder)

	# unzip third party zip file
	zf = zipfile.ZipFile(zipFilePath, 'r', zipfile.ZIP_DEFLATED)
	for oneFile in zf.namelist():
		zf.extract(oneFile, destDir)
	zf.close()

	return

def unzip2FolderUnderLinux(parentPath, folder):
	if len(parentPath) == 0:
		print("The parent path cannot be empty.")
		return

	if len(folder) == 0:
		print("The folder name cannot be empty.")
		return

	destDir = parentPath

	# check zip file
	zipFileName = folder + ".tar.gz"

	zipFilePath = os.path.join(destDir, zipFileName)
	if not os.path.isfile(zipFilePath):
		print("The tar zip file:%s does not exist." %zipFilePath)
		return

	# remove old third party files
	oldFolder = os.path.join(destDir, folder)
	if os.path.isdir(oldFolder):
		shutil.rmtree(oldFolder)

	# unzip third party zip file
	UnzipCommands = "tar zxvf " + zipFilePath + " -C " + destDir + " >/dev/null"
	os.system(UnzipCommands)

	return

def unzip2Folder(parentPath, folder):
	if isLinux():
		unzip2FolderUnderLinux(parentPath, folder)
	elif isWindows():
		unzip2FolderUnderWindows(parentPath, folder)
	return

def runCommand(sCommand):

	returnValue = 0

	if isWindows():
		builder = subprocess.Popen(sCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		builderIter = iter(builder.stdout.readline, b"")
		for output_line in builderIter:
			print(output_line.decode('ascii').strip(), flush=True)

		builder.wait()

		returnValue = builder.returncode
	else:
		returnValue = os.system(sCommand)

	return returnValue


# Generate a temporary folder and then copy src file to the folder
# Return the new file path
def copyToTempFile(src):
	if not os.path.isfile(src):
		return None
	tempFolder = tempfile.mkdtemp()
	fileName = os.path.basename(src)
	pathName = os.path.join(tempFolder, fileName)
	shutil.copy2(src, pathName)

	return pathName

def tagDateVersion(targetPath):
	if not os.path.exists(targetPath):
		return False

	dstFile = os.path.join(targetPath, "dateVersion")
	if os.path.exists(dstFile):
		os.remove(dstFile)

	x = time.strftime("%Y-%m-%d %H:0:0")
	with open(dstFile, 'w') as f:
		f.write(x)

	return True

def getDateVersion(targetPath):
	if not os.path.exists(targetPath):
		return ""

	dstFile = os.path.join(targetPath, "dateVersion")
	if not os.path.exists(dstFile):
		return ""

	with open(dstFile, 'r') as f:
		return f.read()

	return ""