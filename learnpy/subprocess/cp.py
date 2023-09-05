import shutil
import os
import time

path = os.getcwd()
origin = path + "/dir/sub.py"
dest = path + "/sub.py"
time.sleep(3)
print(origin)
print(dest)
shutil.copy(origin, dest)
time.sleep(10)