import pymongo
from sshtunnel import SSHTunnelForwarder

class MongoConn:
    def __init__(self):
        self.mongoHost = "shsirdlnx2"
        self.mongoDb = "database"
        self.server = SSHTunnelForwarder(
            self.mongoHost,
            remote_bind_address=('127.0.0.1', 27017)
        )

    def con(self):
        self.server.start()

        client = pymongo.MongoClient('127.0.0.1', self.server.local_bind_port) # server.local_bind_port is assigned local port
        db = client[self.mongoDb]
        return db

    def disCon(self):
        self.server.stop()
        return None        