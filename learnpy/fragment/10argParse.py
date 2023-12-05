import argparse

# create an object named parser1 to store all the information
parser1 = argparse.ArgumentParser(description="this code is used to get the product of two numbers")

# add two positional argument named a & b
# the default argument type is string
parser1.add_argument("a", type=int, help="this is the first number")
parser1.add_argument("b", type=int, help="this is the second number")

# create a namespace named args1 to store all the positional arguments,which is equal to a dictionary
args1 = parser1.parse_args()

# python 10argParse.py -h : view the help information
sum1 = args1.a * args1.b

print(sum1)
