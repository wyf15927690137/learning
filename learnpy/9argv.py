import imp
import sys
from time import sleep
import requests
print('this is a test file')
print('this is the second line from cloud')
print('this is the second line from cloud1')
print('this is the third line from Local')
print('this is the third line from Local1')
sleep(2)
s1 = sys.argv[1]
s2 = sys.argv[2]
s3 = sys.argv[3]
sys.argv.append("Lux")
print(sys.argv[0])  # return current file path
print(s1)
print(s2)
print(type(s3))  # view the datatype
sleep(3)
s4 = int(s3)
print(type(s4))
print(int(s2) * int(s3))
print(sys.argv)
sleep(2)
