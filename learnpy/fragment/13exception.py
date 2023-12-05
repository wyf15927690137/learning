# exception
num1 = 5
num2 = 'abc'
num3 = 0
try:
    # num4 = num1 / num2
    num5 = num1 / num3
except ZeroDivisionError:
    print("the divisor is 0")
except TypeError:
    print("the type error")
else:
    print("there is no exception")