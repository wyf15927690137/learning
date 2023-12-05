import pymongo
import time
# pymongoclient = pymongo.MongoClient("mongodb://admin:123456@shsirdlnx1/database")

# defaults to port 27017, db = client.animals
# print the number of documents in a collection
# sameURL (MongoClient) can help to connect via NODEJS.
# db = pymongoclient['database']
# table = db['finishedIdList']
# print(table.find()[0])
# pymongoclient.close()
pymongoclient1 = pymongo.MongoClient("mongodb://admin:123456@shsirdlnx1/database")
db = pymongoclient1['database']
table = db['finishedIdList']
print(table.find()[0])
time.sleep(5)
pymongoclient1.close()
time.sleep(30)
