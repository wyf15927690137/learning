import os
import shutil

# Providing the folder path
origin = r'D:\Test\1'
target = r'D:\Test\2'

def getCaseName(casePath):
    s = ""
    # iterate a string reversely
    for x in reversed(casePath):
        if x != '\\':
            s = x + s
        else:
            break
    return s
    
products = ["opi.txt", "psi.txt", "pwt.txt","xim.txt"]
# "pdc.txt",
for product in products:
    s_file = open(product,"r",encoding='UTF-8')
    all_content = s_file.read()
    lines = all_content.split('\n')
    num = len(lines)-1
    print(f"there are {num} cases")

    target = lines[0]
    print(f"the target path is {target}")
    if os.path.exists(target):
    #     # remove empty dir
    #     # os.rmdir(target)
        shutil.rmtree(target)
        print(f"target path {target} is deleted")
    os.makedirs(target)
    print(f"empty target path {target} is created")

    # print(lines[1:])

    for case in lines[1:]:
        casename = getCaseName(case)
        targetcase = os.path.join(target,casename)
        shutil.copytree(case, targetcase)
        print(f"{case} is copied successfully")
