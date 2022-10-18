import sys
import os
print(sys.path)
print("================")
print(sys.path[0])
print("================")
print(os.path.dirname(sys.path[0]))
print("================")
print(os.listdir(sys.path[0]))


dest_dir = os.path.dirname(sys.path[0])
print(dest_dir)