import os
for (dirpath, dirnames, filenames) in os.walk("D:\PersonalLearn\learning\learnpy\os"):
    print(dirpath)
    print('-----')
    print(dirnames)
    print('------')
    print(filenames)
    print("=======")