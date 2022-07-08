#!/bin/sh
# output every commandline before excuting
# set -x

# exit the current script when meet errors
#set -e
echo test
cd /wyf
# echo test1
if (test "$?" == "0")
then
echo last command executed successfully
else 
echo last command executed error
fi

echo test1