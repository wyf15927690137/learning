from pymongo import MongoClient
from urllib.parse import quote_plus

# Replace the connection details with your remote MongoDB server information
username = "yanfeiw"
password = "Yfw@1997"
host = "10.134.176.64"
port = 27017
db_name = "database"
mongoUrl = f"mongodb://{quote_plus(username)}:{quote_plus(password)}@{host}:{port}/{db_name}?authSource=admin"
# mongoUrl = f"mongodb://{username}:{password}@{host}:{port}/{db_name}?authSource=admin"

client = MongoClient(host='shsirdlnx2')
db = client["database"]
table = db['workingBuildList']
items = table.find()
for item in items:
    print(item)