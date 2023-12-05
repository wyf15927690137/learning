from utilForMongo import MongoConn

mongo = MongoConn()
i = 15
while i > 0:
    db = mongo.con()
    table = db['workingBuildList']

    print(table.find()[0])
    mongo.disCon()
    i-=1
