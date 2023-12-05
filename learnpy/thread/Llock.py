# pip install pymongo
import pymongo
import threading

class jobList:
    def __init__(self):
        self.__list = {}
        self.__lock = threading.Lock()
        self.__db = None
        self.__jobTable = None

    def initDB(self):
        print("init db")
        client = pymongo.MongoClient(host='127.0.0.1')
        self.__db = client['database']
        if self.__db:
            print("create table")
            self.__jobTable = self.__db['jobTable']
        
    def insertItem(self):
        with self.__lock:
            if not self.__list:
                return
        
        self.__jobTable.insert_one(self.__list)
        print("item inserted")

    def removeItem(self):
        with self.__lock:
            if not self.__list:
                return
        
        self.__jobTable.delete_one(self.__list)
        print("item deleted")

if __name__ == "__main__":
    job = jobList()
    job.initDB()
    job.__list = {"name": "yf", "age": "22"}
    job.insertItem()
