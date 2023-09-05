import datetime
import time

# 2022-11-29 17:02:25.641913
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

date1 = datetime.datetime.strptime("202234",f'%Y%m%d')
print(f"date1: {date1}")
t = '20220304'
t = int(time.mktime(time.strptime(t,"%Y%m%d")))
print(t)