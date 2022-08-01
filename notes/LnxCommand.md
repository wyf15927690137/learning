view disk space info

```
df
```

copy folder A to B

```
cp /../../A /../../B -r
```

call a makefile in a specific path, do make action:

```sh
make -C /data/users/yanfei/yanfeiw_main/Programs/ClarityTools/Trinity_script/conan_cythonizer
make -C /data/users/yanfei/yanfeiw_main/Programs/ClarityTools/Trinity_script/conan_cythonizer clean
```

change file permission:

```
chmod u+x file1
chmod a+x file2
chmod ug+x file3
chmod 777 file	r=4 w=2 x=1
```

view compressed file

```
gtar -tvf **.tar.gz
```

tar

```
tar zvxf *.tar.gz
tar -xvf *tar.xz 
```

change the permission of a folder

```
chmod 777 folder -R
```

switch user in linux

```
su - root
su - yanfeiw
#use cc.key to login cc account without password
ssh sjf-cpgmsa10 -l cc -i cc.key
```

wget

```
sudo apt install wget
sudo yum install wget
wget  https://cmake.org/files/v3.15/cmake-3.15.7.tar.gz
```

tee:  

```sh
tee (-a) <file>	#input into a file
echo test | tee -a <file>	#output into a file 	"-a" means append
```

p4 command：

```sh
p4 clean -a -d -e:
-a
Added files: Find files in the workspace that have no corresponding files in the depot and delete them.
-d
Deleted files: Find those files in the depot that do not exist in your workspace and add them to the workspace.
-e
Edited files: Find files in the workspace that have been modified and restore them to the last file version that has synced from the depot.

#sync code as workspace view, will delete other code
p4 sync

p4 set P4CLIENT=yanfeiw_shcpgrdwin1_new
p4 set P4PORT=ssl:p4shanghai:2644
p4 sync -f:(p4 clean -d -e)
p4 sync //depot/sigrity/main/Install/cm/jenkins_utils/...
overwrite the existed files,don't overwrite files checked out

#refreshing all the edited files and missing files(except checked out files)
p4 sync -f //depot/sigrity/main/Install/cm/jenkins_utils/...
p4 clean -a //depot/sigrity/main/Install/cm/jenkins_utils/...
p4 set
p4 set P4PORT= xx.xxx.xx.xxx:xxxxx
p4 set P4USER=username
p4 set P4PASSWD=yourpasswd
p4 set P4CLIENT=nameofworkspace

```

windows \r\n problem:

```sh
sed -i "s/\r//" ****.sh
```

copy folders from one server to another

```
scp -r cc@sjf-cpgmsa10:/Software/Python3 ./Files
```

```sh
 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 python3 get-pip.py
```

find a process and kill it

```sh
ps aux | grep "gunicorn"
kill -r processid
```

find processes contains string "pem -b :5000", cut -c 9-15 will get the processes id, xargs will make the process ids as the input parameter as kill -9

```sh
ps aux | grep "pem \-b :5000" | cut -c 9-15 | xargs kill -9
```

ssh login remote linux server without password

```sh
ssh-copy-id -i ~/.ssh/id_rsa.pub shsirdlnx2
```
