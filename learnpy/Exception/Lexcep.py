from utilForMongo import MongoConn


def main():
    try:
        mongo = MongoConn()
        client = MongoConn().con()
        table = client['workingBuildList']
        items = table.find()
        print(items[0])
        try:
            mongo = MongoConn()
            client = mongo.con()
            table = client['workingBuildList']
            items = table.find()
            print(items[0])
            print(x)
        except Exception as err:
            print("err:" + str(err))
        finally:
            print("this is finally")
            mongo.disCon()
    except Exception as err:
        print("another err")
    finally:
        print("another finalyy")

main()