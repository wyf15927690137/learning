from threading import Timer
import time

def fun1():
    print("this is a test file")
    Timer(interval,fun1).start()

interval = 1
Timer(interval,fun1).start()