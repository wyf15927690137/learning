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

for item in collections.find():
    print(item)
#  only update the first document that matches the filter.
# If you want to update multiple documents, you can use update_many() instead.
collections.update_one(
    {'name': "yfw"},
    {'$set': {'age': '25'}}
)

db = client['database']
table = db['workingBuildList']
items = table.find()
for item in items:
    print(item)
# count the items matches
count = table.count_documents({'jiraIssue': 'SBH-136'})
print(count)


server.stop()