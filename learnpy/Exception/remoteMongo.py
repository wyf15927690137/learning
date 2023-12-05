from pymongo import MongoClient


class MyDB:
    def __init__(self):
        self.__mongoCon = None
        self.__db = None
        self.table = None

    
    def InitDB(self):
        self.DBOpen()
        if self.__db is not None:
            self.table = self.__db['table1']
        print(len(list(self.table.find())))
        for x in self.table.find():
            print(x)
        self.DBClose()


    def DBOpen(self):
        if self.__db is None:
            self.__mongoCon = MongoClient("mongodb://admin:123456@shsirdlnx1/database")
            self.__db =  self.__mongoCon['database']
    def DBClose(self):
        self.__db = None
        self.__mongoCon.close()
        self.__mongoCon = None


mydb = MyDB()
mydb.InitDB()
mydb.DBOpen()
mydb.DBClose()
mydb.InitDB()