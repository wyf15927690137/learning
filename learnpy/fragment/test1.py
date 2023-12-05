import datetime as dt
import time
t1 = dt. datetime. strptime('12:00:00', '%H:%M:%S')
t2 = dt. datetime. strptime('02:00:00', '%H:%M:%S')
time_zero = dt. datetime. strptime('00:00:00', '%H:%M:%S')
print((t1 - time_zero + t2).time())

time.sleep(3)
print((t1 - time_zero + t2).time())
time.sleep(3)
print((t1 - time_zero + t2).time())
time.sleep(3)
print((t1 - time_zero + t2).time())