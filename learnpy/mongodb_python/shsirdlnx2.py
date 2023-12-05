import pymongo
from sshtunnel import SSHTunnelForwarder
import time

MONGO_HOST = "shsirdlnx2"
MONGO_DB = "database"

try:
    server = SSHTunnelForwarder(
        MONGO_HOST,
        # ssh_username=MONGO_USER,
        # ssh_password=MONGO_PASS,
        remote_bind_address=('127.0.0.1', 27017)
    )

    server.start()

    # connect to remote mongodb
    client = pymongo.MongoClient('127.0.0.1', server.local_bind_port) # server.local_bind_port is assigned local port
    db = client[MONGO_DB]

    db_list = client.list_database_names()
    print(db_list)


    table = db['workingBuildList']
    items = table.find()
    for item in items:
        print(item)
except Exception as err:
    print(str(err))
finally:
    server.stop()
    time.sleep(100)