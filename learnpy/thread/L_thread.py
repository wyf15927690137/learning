import threading
from time import sleep

def job():
    sleep(5)
    print("the number of T1 is %s" %threading.current_thread)
    return

print("the active thread number:", threading.active_count())
print("the info of all the current thread:", threading.enumerate())
print("the info of the current thread:", threading.current_thread())