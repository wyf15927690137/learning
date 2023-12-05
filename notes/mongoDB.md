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
db.person.drop() (drop the tabel 'person')


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



# how to install mongodb on linux:

```
touch /etc/yum.repos.d/mongodb-enterprise-7.0.repo

```

```
[mongodb-enterprise-7.0]
name=MongoDB Enterprise Repository
baseurl=https://repo.mongodb.com/yum/redhat/$releasever/mongodb-enterprise/7.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-7.0.asc
```

```
sudo yum install -y mongodb-enterprise
sudo yum install -y mongodb-enterprise mongodb-mongosh-shared-openssl11
```

"Failed to unlink socket file","attr":{"path":"/tmp/mongodb-27017.sock","error":"Operation not permitted

```
delete this file
```



# View mongodb remote connection:

```
 netstat -apn | grep 27017
```



# Config remote mongodb:



```
show dbs
use database
db.createUser({
 user: 'admin',
 pwd: '123456',
 roles: [{ role: 'readWrite', db:'database'}]
})
show usersm
```

```
sudo vim /etc/mongod.conf

# network interfaces
net:
  port: 27017
  bindIp: 0.0.0.0  <- update this line
  
security:
  authorization: 'enabled'
```

```
sudo service mongod restart
tail -f /var/log/mongodb/mongod.log
```

```
mongo -u admin -p 123456 shsirdlnx1/database
mongosh -u admin -p 123456 shsirdlnx1/database
```

```
import pymongoclient = pymongo.MongoClient("mongodb://hardeep:yourSecretPassword@169.45.23.99/animals")
# defaults to port 27017, db = client.animals
# print the number of documents in a collection
# sameURL (MongoClient) can help to connect via NODEJS.
print db.animals_collection.count()
```

```

```

