import argparse
from time import sleep
from threading import Timer

argp = argparse.ArgumentParser(description="this code is used to get the product of two input numbers")

argp.add_argument("a",type=int,help="the first input number")
argp.add_argument("b",type=int,help="the second input number")

pargs = argp.parse_args()

output = pargs.a*pargs.b

print(output)

sleep(2)

interval = 1 

def myprint():
    print("this is a test line")
Timer(interval,myprint).start()
sleep(4)