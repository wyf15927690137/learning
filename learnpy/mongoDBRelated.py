import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# database will be created only after the data inserted
mydb = myclient["database"]
dblist = myclient.list_database_names()

if "database" in dblist:
    print("the database already exsited")

# table
mycol = mydb["one"]
tablist = mydb.list_collection_names()
if "one" in tablist:
    print("table already exsited")

example1 = {"name": "one", "value":2}
x = mycol.insert_one(example1)
print(x)

mycol2 = mydb["two"]
example2 = {"name": "two", "value":3}
y = mycol2.insert_one(example2)
print(y.inserted_id)
print(mycol.find())






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