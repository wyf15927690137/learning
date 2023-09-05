# pip install pymongo
import pymongo
client = pymongo.MongoClient(host='127.0.0.1')

db_list = client.list_database_names()
print(db_list)

# db = client['traffic']
# collections = db['person']
# new_db_list = client.list_database_names()
# print(new_db_list)

# person1 = {'name': 'yfw',
#            'age': '26',
#            'height': '185'}
# result = collections.insert_one(person1)
# print(result)
# print(result.inserted_id)

# collections.update_one(
#     {'name': "yfw"},
#     {'$set': {'age': '25'}}
# )
col = client['database']
x = col['workingBuildList']
y = x.find()
for z in y:
    print(z)