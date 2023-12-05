import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', nargs='+', type=str, help='changelists list')
parser.add_argument('-u', type=str, help='username')
parser.add_argument('-p', type=str, help='p4 port')

params = sys.argv[1:]
args = parser.parse_args(params)
changelists = args.c
username = args.u
p4port = args.p
print(changelists)
print(username)
print(p4port)
time.sleep(30)