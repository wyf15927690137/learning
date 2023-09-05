import pymongo
from sshtunnel import SSHTunnelForwarder

MONGO_HOST = "shsirdlnx2"
MONGO_DB = "database"

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

db = client['traffic']
collections = db['person']
new_db_list = client.list_database_names()
print(new_db_list)

person1 = {'name': 'yfw',
           'age': '26',
           'height': '185'}
result = collections.insert_one(person1)
print(result)
print(result.inserted_id)
counts = collections.count_documents({'name':'yfw'})
print(counts)


# item1 = {"batchId" : "25008c45-55be-404f-b0fd-2ecf461f8b75", "processing" : 1, "finished" : 0 }
item2 = {"batchId" : "153d0326-85f9-4526-a5ab-e2b2e87e8fb3", "processing" : 1, "finished" : 0 } 
# item3 = {"batchId" : "153d0326-85f9-4526-a5ab-e2b2e87e8fb3", "buildId" : "f043a649-4cdc-4d9c-8818-7baf02fd7636", "ccrNumber" : "2744213", "jiraIssue" : "", "project" : "allproject", "platform" : "linux", "finished" : 1, "testResult" : "Build complete!", "ratio" : 1, "passStatus" : "DREG-PASSED:12345-FAILED:0", "jenkinsId" : 18879, "version" : "main", "changeList" : "411834" }
db = client['database']
tables = db['workingIdList']
table2 = db['workingBuildList']
# result1 = tables.insert_one(item1)
result1 = tables.insert_one(item2)
# table2.insert_one(item3)
# result1 = tables.insert_one(item3)
# db = client['database']
# tables = db['workingBuildList']
#  only update the first document that matches the filter.
# If you want to update multiple documents, you can use update_many() instead.
# collections.update_one(
#     {'name': "yfw"},
#     {'$set': {'age': '25'}}
# )

# db = client['database']
# table = db['workingBuildList']
# items = table.find()
# for item in items:
#     print(item)
# # count the items matches
# count = table.count_documents({'jiraIssue': 'SBH-136'})
# print(count)


server.stop()