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

tar

```
tar -xvf archive.tar.xz -C ./
tar -xvzf fafa.tar.gz -C ./
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

view python modules

```
python3
help("modules")
```

find a process and kill it

```sh
ps aux | grep "gunicorn"
kill -r processid
```

update git on linux

```sh
wget -O v2.24.1.tar.gz https://github.com/git/git/archive/v2.24.1.tar.gz
tar -xzvf ./v2.24.1.tar.gz
```

view files number & size

```shell
du -s (directorypath)	#number
du -sh  (directorypath)	#size
```

source a script: execute the script in current shell env

```shell
source test.sh
```

use python pip in linux

```
which python
python -m pip -V
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
python -m pip install flask
```

install dask

```
python -m pip install "dask[complete]"
add ~/.local/bin into PATH
```

disk free space:

```
df
```

view ip info

```
ifconfig (sudo apt install net-tools)

hostname -I
```

```

```

create and uncompress a tar archive file (folder)

```
tar -cvf test.tar /home/test/
tar -cvf test.tar test.txt
tar -zcvf test.tar.gz /home/test/
tar -zcvf test.tar.gz test.txt
tar zvxf *.tar.gz
tar -xvf *tar.xz 
```

view compressed file

```
gtar -tvf **.tar.gz
```



&&, &, |, ||

```
&: background

# if cmd1 succeed, then cmd2
cmd1 && scmd2

# the output of cmd1 as the input of cmd2
cmd1 | cmd2

# if cmd1 failed, then cmd2
cmd1 || cmd2
```



# Service Related:

```sh
chkconfig --list
systemctl list-unit-files
systemctl status sshd.service
```

```sh
#append
echo -e "test" >> a.txt
#overwrite
echo -e "test" > b.txt
```

# Some often used cmd:

## Link (symbolic (soft) , hard ):

```sh
# symbolic (soft) link
ln -s filename(foldername) linkname
```

![img](https://img-blog.csdnimg.cn/img_convert/58ef0e77013fbd6bc7be56d18aef440c.png)

```sh
# hard link
ln filename linkname
```

## scp:

```
scp -r hello-python/ yanfeiw@shsirdlnx1:/data/yanfeiw/kubernetes
```

## novnc:

```sh
# use current machine 6081 listen shsirdlnx1:6902
novnc_proxy --vnc shsirdlnx1:6902 --listen 6081
novnc_proxy --vnc shsirdlnx2:30001
```

## change owner:

```sh
# chown username:group
sudo chown yanfeiw:cadence_2 test_gui_image.tar
sudo chown -R yanfeiw:cadence_2 <Foldername>
chown newowner filename 
chown newowner foldername -R
# change mod
sudo chmod 755 <filename>
sudo chmod -R 755 <filename>
```

## find processes contains string "pem -b :5000", cut -c 9-15 will get the processes id, xargs will make the process ids as the input parameter as kill -9

```sh
ps aux | grep "pem \-b :5000" | cut -c 9-15 | xargs kill -9
```

## ssh login remote linux server without password

```sh
ssh-copy-id -i ~/.ssh/id_rsa.pub shsirdlnx2
ssh shsirdlnx2 -i id_rsa
```

## how to use VNC viewer

```
vncserver -depth 24 -geometry 2560x1440
shsirdlnx2:2
/grid/common/pkgs/perforce/latest/bin/p4v&

# kill the first vnc process
vncserver -kill :1

# change the password
vncpasswd
```

## view sys mem info:

```sh
# kB
free
# Mb
free -m
# Gb
free -h
```

![image-20230224101950430](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20230224101950430.png)

```sh
available = free + buff/cache
total = used + available
# buff : hass yet to be "written" to disk
# cache: "read" from disk and stored for later use
```

## view sys cpu info:

```
cat /proc/meminfo
cat /proc/cpuinfo
```

```sh
# 总核数 = 物理CPU个数 X 每颗物理CPU的核数 
# 总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数

# 查看物理CPU个数
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l

# 查看每个物理CPU中core的个数(即核数)
cat /proc/cpuinfo| grep "cpu cores"| uniq

# 查看逻辑CPU的个数
cat /proc/cpuinfo| grep "processor"| wc -l
```

# Install Node.js and npm on centos7:

```
wget https://rpm.nodesource.com/setup_10.x
mv setup_10.x config.sh
bash config.sh
sudo yum install nodejs
sudo yum remove -y nodejs npm
sudo yum list available nodejs
sudo yum install <package name>-<version info>
yum --showduplicates list httpd | expand
npm config set registry=https://registry.npm.taobao.org
```

# Use yum:

```sh
ll /etc/yum.repos.d
```

```
cat /etc/yum.repos.d/c0700_r7.repo
```

```
sudo yum -y remo
ve mariadb-libs
```

## Trigger Jenkins job through curl (also works in windows cmd):

```
curl -X post http://master-sigrity.cadence.com:9090/job/AutoBuild/job/CheckCM/buildWithParameters?token=BDEE94C3-AC22-4366-8ADF-1DDB62D989BA -F username=cc -F BuildVersion=23.10.0314.413861 -F EndChange=413861
```





# rsync through ssh without password:

```sh
# if can use rsync ssh
rsync -avz -e ssh svc_cicd@si-rdtest1:/vols/sigrity_fort03/SIG/CM/kits/23.10main/23.10.0328.416227/lnx86/sigTopXpInt /data/Automation/AutoBuild/TopXP_23.10_main/LocalBuild
# input password
Shang@123

rm -rf ./

ssh-copy-id -i ~/.ssh/id_rsa.pub si-rdtest1
rsync -avz -e ssh svc_cicd@si-rdtest1:/vols/sigrity_fort03/SIG/CM/kits/23.10main/23.10.0328.416227/lnx86/sigTopXpInt /data/Automation/AutoBuild/TopXP_23.10_main/LocalBuild
```

# view the disk usage of  disk or directory

```
df -h
du -sh /path/to/directory
du -h
du -sh
```

shell and csh

```sh
# sh
export PATH=/usr/bin:$PATH
# csh
setenv PATH "/usr/bin:$PATH"
```

# view linux Process

```
ps -u yanfeiw
# a: all u: cpu mem etc..  x: damneo
ps aux

```

cat os version

```
cat /etc/os-release
```

View port used

```
 lsof -i:8888
 ps aux | grep 374113
 kill 374114
```

```
# view lnx os version
cat /etc/os-release 
```

```
uname : Linux
uname -m : x86_64
```

# How to use .bashrc

```
https://www.digitalocean.com/community/tutorials/bashrc-file-in-linux
```

fix warnnig:

```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
    LANGUAGE = "en_US:en",
    LC_ALL = (unset),
    LANG = "en_US.ISO-8859-1"
are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
```

vim ~/.bashrc

```
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```



# port used

```
  File "/data/users/yanfei/Files/Python3/Python-3.7.9/Lib/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
```

```
sudo lsof -i :6000
```

# SSH Error:

```
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:P6ac7bl0aUCOZrHpmqGue9T5IRtMu0rmwMM8kLGsCGs.
Please contact your system administrator.
Add correct host key in /home/yanfeiw/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /home/yanfeiw/.ssh/known_hosts:2
  remove with:
  ssh-keygen -f "/home/yanfeiw/.ssh/known_hosts" -R "shsirdlnx2"
Host key for shsirdlnx2 has changed and you have requested strict checking.
Host key verification failed.
```

```
  ssh-keygen -f "/home/yanfeiw/.ssh/known_hosts" -R "shsirdlnx2"
```

## Assgin  the output of a linux cmd to a variable:

```
variable_name=$(command)
variable_name=$(command [option ...] arg1 arg2 ...)
OR
variable_name='command'
variable_name='command [option ...] arg1 arg2 ...'
```

# Shell String manipulation(how to intercept string):

```
https://www.geeksforgeeks.org/string-manipulation-in-shell-scripting/#
```

# Use curl to access jira API

```
curl -u svc_cicd:Shang@123 -X GET -H "Content-Type: application/json"  https://jira.cadence.com/rest/api/2/issue/FIDELITY-39

c3ZjX2NpY2Q6U2hhbmdAMTIz

curl -H "Authorization: Basic c3ZjX2NpY2Q6U2hhbmdAMTIz" -X GET -H "Content-Type: application/json"  https://jira.cadence.com/rest/api/2/issue/FIDELITY-39/comment/1

curl -H "Authorization: Basic c3ZjX2NpY2Q6U2hhbmdAMTIz" -X GET -H "Content-Type: application/json" https://jira.cadence.com/rest/api/2/issue/SIG-315/comment | jq '.comments' | jq '.[] | .body' | tail -1

```

# Install python on ubuntu:

```
sudo apt-get wget 
wget https://www.python.org/ftp/python/3.9.17/Python-3.9.17.tar.xz
tar -xvf Python-3.9.17.tar.xz
```

# If a file exists:

```sh
# if file exists and is a directoty
test -d
# if file exists and is a regular file
test -f
# if file exists (regardless of type: directory or file)
test -e
# test: Evaluate a conditional expression
test -1 -gt -2 && echo yes
	yes
```

```
#!/bin/sh
# the number of parameters
echo "number:$#"
echo "scname:$0"
echo "first :$1"
echo "second:$2"
# the parameter list
echo "argume:$@"
# all parameter
echo "show parm list:$*"
echo "show process id:$$"
# the exit status of last cmd
echo "show precomm stat: $?"

# if the env is defined
$?JenkinsCI	
```

reboot and poweroff:

```
sudo reboot
sudo poweroff
```

