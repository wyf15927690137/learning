import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# database
mydb = myclient["database"]
# table
mycol = mydb["testOne"]

def IfSendPostToOneBuild(id):
    try:    
        mydb = myclient["database"]
        if not mydb:
            return

        mycol = mydb["testOneBuild"]
        if not mycol:
            return 


        mycol.create_index([("batchid",pymongo.ASCENDING)],unique=True)
        mycol.insert_one({"batchid":str(id)})
        print("create index and insert batchid succeed!")

    except Exception as e:
        print("index already existed, insert batchid failed!")
    return 

def query(id): 
    batchidinfo = {"batchid":id}
    for x in mycol.find({},{"_id":0,"batchId":1}):
        if(x == batchidinfo):
            print("already triggered this job, don't need to trigger again!")
            return
    else:
        mycol.insert_one(batchidinfo)
        mycol.find_one_and_update
        print("haven't triggered this job, start to send a post!")
        # SendPostToOneBuild(processor)
        return