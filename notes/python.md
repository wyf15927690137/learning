download get-pip.py

python get-pip.py install

add python.exe to path

add ./script/pip.exe to path

use pip to install 3rd party

pip install flask
pip uninstall jira

pycharm：

pip install cryptography -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

pip install --upgrade pip -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com



/usr/bin/python: bad interpreter: No such file or directory 

```
sudo ln -s /usr/bin/python2.4 /usr/bin/python
```







# gunicorn

```sh
-w : The number of worker processes. This number should generally be between 2-4 workers per core in the server. 
-t (timeout):  Workers silent for more than this many seconds are killed and restarted.
-b : the socket to bind
	-b: 5000
	
gunicorn -w 12 -t 240 start:app --certfile ./https_key/cert.pem --keyfile ./https_key/key.pem -b :5000 2>&1 | tee start.log
```

permission denied:

```
#!/usr/local/bin/python
-->
#!/usr/bin/env python
```

# P4

```
#linux
 python -m pip install p4python 
#windows
python -m pip install p4
```

# How to Config python on linux:

```sh
wget https://www.python.org/ftp/python/3.7.16/Python-3.7.16.tar.xz
tar -xvf Python-3.7.16.tar.xz -C ./
mkdir MYPython
cd Python-3.7.16
./configure --prefix=MYPython
make
make test
make install

#cd MYPython and find python binary, add into PATH
mkdir lib_linux
cd lib_linux
# specify the python packege location
python -m pip install jira -t .
python -m pip install p4python -t .
```

Sys.path is a list of directories where the Python interpreter searches for modules. Mind you, this is a list! When a module is claimed in a project file, it will search through each one of the directories in the list. If the module is located within one of those directories, then everything goes fine and your project is successfully rendered. However, if the module is not located within any of the listed directories, then your project will fail lest you can “append” the directory where your module is located to the list using the append() function. In this tutorial, we’ll be learning about how to use sys.path.append() in Python.

```py
import os
import sys
# python scripts use the packages in a specified path
sys.path.append(os.getcwd() + "/lib_linux")
from P4 import P4, P4Exception
from jira import JIRA
import base64
```

GitPython:

```
python -m pip install GitPython
```

# AWS S3

```
Connecting to AWS S3 with Python:
https://www.gormanalysis.com/blog/connecting-to-aws-s3-with-python/
```

Portable python

```
https://github.com/indygreg/python-build-standalone/releases

# use pip in this portable python, the packages can auto install and load
```





The function of some ENV for python:'

```
#!/usr/bin/env bash

curScriptFolder=$(dirname "$(readlink -f "$0")")
export PATH=${curScriptFolder}/bin_linux/python3.10.12/install/bin:$PATH
# python can find some system lib from this env, such as libtk.so
export LD_LIBRARY_PATH=${curScriptFolder}/bin_linux/python3.10.12/install/lib:$LD_LIBRARY_PATH
# python can find the modules in this path, such as : import P4, import P4API
export PYTHONPATH=${curScriptFolder}/bin_linux/python3.10.12/install/lib/python3.10/site-packages

python3 ${curScriptFolder}/start.py $@

```

