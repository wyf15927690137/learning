# start mongod svc and specify db path and log path:

```sh
mongod --dbpath /data/users/yanfei/Files/mongodb/data --logpath /data/users/yanfei/Files/mongodb/log/mongodb.log --fork
# --fork
	: run a mongod process as a daemon
# stop mongod
pkill -9 mongod
```

```sh
show dbs
# create db or use db
use traffic
# view the current db
db
# delete the current db
db.dropdDatabase()
# show tables
use traffic
show tables
# create table
db.createCollection('table1')
# delete table
db.table1.drop()
# insert entry
db.table1.insert({"name":"fly","age":"22"})
# drop all entries
db.table1.remove({})
```

```sh
# view mongodb config
vim /etc/mongodb.conf

# restart mongodb service
systemctl restart mongod

# some command
show users
show dbs

use local
show tables
show collections
db (show current db)

db.dropDatabase()
use traffic (use this database)
db.person.find() (view all the entry)
db.person.find({'name':'yfw'})
db.person.drop (drop the tabel 'person')


serivce mongod start
serivce mongod status
# stop mongod
service mongod stop
```



remote connect 

```
use admin
db.createUser(
      {
          user: "svc_cicd",
          pwd: "Shang",
          roles: [ "root" ]
      }
  )
```

