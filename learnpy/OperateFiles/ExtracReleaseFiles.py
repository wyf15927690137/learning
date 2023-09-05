from cgi import print_arguments
import sys
import os
import json
import platform
import utility

argvSize = len(sys.argv)
if argvSize < 2 :
	print("Please input the path of the current WORKSPACE!")
	sys.exit(1)

if argvSize < 3 :
	print("Please input the name of the Json file!")
	sys.exit(1)

WORKSPACE = sys.argv[1]
JsonFileName = sys.argv[2]
print("the current workspace is:" + WORKSPACE)

CurrentRealPath = os.path.realpath(__file__)
CurrentDirectoryPath = os.path.split(CurrentRealPath)[0]
JsonFilePath = os.path.join(CurrentDirectoryPath,JsonFileName)

with open(JsonFilePath,"r") as read_ProductLists:
	ProductLists = json.load(read_ProductLists)

product_name = ""
project_name = []
project_source = ""
project_target = ""
project_platform = ""
project_num = 0

for module_name,module_products in ProductLists.items():
	print("start  to extract %s module!" %module_name)
	for one_product in module_products:
		for product_info in one_product.items():
			if product_info[0] == "Product":
				product_name = product_info[1]
			if product_info[0] == "Product Info":
				for project in product_info[1].items():
					project_platform = project[0]
					if project_platform == platform.system():
						for projects_info in project[1].items():
							if projects_info[0] == "Project Name":
								project_name = projects_info[1]
							if projects_info[0] == "Source Path":
								project_source = projects_info[1]
							if projects_info[0] == "Target Path":
								project_target = projects_info[1]

						project_num = len(project_name)
						project_sourcedir = os.path.join(WORKSPACE,project_source)
						project_targetdir = os.path.join(WORKSPACE,project_target)
						while project_num > 0 :
							print("start to extract %s project on %s platform!" %(project_name[project_num-1],project_platform))
							if not os.path.isdir(project_targetdir):
								os.makedirs(project_targetdir)
							sourceFile = os.path.join(project_sourcedir,project_name[project_num-1])
							if os.path.isdir(sourceFile):
								print("This is a directory!")
								destFileDir = os.path.join(project_targetdir, project_name[project_num-1])
								if not os.path.isdir(destFileDir):
									os.makedirs(destFileDir)
								utility.copyTreeToDirectory(sourceFile, destFileDir)
							else:
								utility.copyFileToDirectory(sourceFile, project_targetdir)				
							project_num-=1
							
sys.exit(0)