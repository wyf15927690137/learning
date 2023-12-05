import os
# os.system execute the operation system command
os.system("echo this is a test")
os.system("dir")
os.system("echo %WORKSPACE%")
os.system("start ./test/test.bat")
exit(1)
# get current file path
cwd=os.getcwd()
print(cwd)

# r prefix in python : all string will be treated as a raw string
print('input\n')
print(r'input\n')

# f prefix in python : get the value of a variable
name = 'wyf'
print(f'{name}')
print("================")

# get the files list of a folder
dic = os.listdir("D:\PersonalLearn\learning")
print(dic)
print("================")

# travel all the files of a folder
for path,dirs,files in os.walk("D:\PersonalLearn\learning\learnbat"):
    print(path)
    print(dirs)
    print(files)
# get operation system type   win: nt   linux: posix
print(os.name)