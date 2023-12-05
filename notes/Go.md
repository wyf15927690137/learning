```sh
# workspace gowiki
go mod init yanfeiw/gowiki
# go workspace
src
bin

# change the path of imported packge
go mod edit --replace example.com/greetings=../greetings
# check the imported packge
go mod tidy
# run the main packge and main function
go run .
# build binary under the current folder
go build
# install the binary to the specified go path
go list -f '{{.Target}}'
go env -w GOBIN=/data/users/yanfei/Files/learning/learngo/bin
go env | grep GOBIN
go install
# get dependencies for code in the current directory
go get .
# build the binary to the current folder
go build wiki.go
```



# Gin-vue-admin:

```sh
# add a new api
server/api/v1/myTest
server/initialize
server/router
server/service
web/src/api
web/view/my
```

# tcp :8888: bind: address already in use 

```
sudo lsof -i -P -n | grep LISTEN
```

```
nil is the zero value for pointers, interfaces, maps, slices, channels and function types, representing an uninitialized value.
```

# How to create go modules:



![](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20230404170347282.png)

1.

```sh
cd packages
touch create_yaml.go
```

create_yamls.go

```go
package packages
.....
```

```sh
go mod init k8sApi/packages
```

2.

```
cd start
touch start.go
```

start.go

```go
package main

import (
	"k8sApi/packages"
)
```

```
go mod init k8sApi/start
go mod edit --replace k8sApi/packages=../packages
go mod tidy
go run start.go
```

3.

main.go

```go
package main

import (
	"k8sApi/packages"
)
```

```
go mod init k8sApi/main
go mod edit --replace k8sApi/packages=./packages
go mod tidy
go run main.go
```





how to add a new api in gin-vue-adm: 

```
# web:
/gin-vue-admin-debug/web/src/view/my/index1.vue
/gin-vue-admin-debug/web/src/api/test.js

# server:
/data/users/yanfei/Files/gin-vue-admin-debug/server/service/myTest
/data/users/yanfei/Files/gin-vue-admin-debug/server/router/myTest
/data/users/yanfei/Files/gin-vue-admin-debug/server/initialize/router.go
/data/users/yanfei/Files/gin-vue-admin-debug/server/api/v1/myTest

Initialize --- router --- api ---- service

               Vue----js
```

Install go on linux:

```
wget https://go.dev/dl/go1.20.5.linux-amd64.tar.gz
```

start millenium on windows

![image-20230710153404061](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20230710153404061.png)

debug millennium on linux:

![image-20231103100842579](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20231103100842579.png)

The breakpoint here will not work, put the breakpoint inside the api

![image-20231031165518403](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20231031165518403.png)

We can start the server first, and then set the breakpoint
