#!/bin/sh
CMRoot=$1
CMPrefix=$2
CMList=`ls -lrt $CMRoot | awk '{print $NF}'`
for item in $CMList
do
    if [[ "$item" == "$CMPrefix"* ]]; then
        if test -f "$CMRoot/$item/good.build"; then
            CMVersion=$item
        fi
    fi
done

echo $CMVersion

SPBRoot=$3
SPBPrefix=$4
SPBList=`ls -lrt $SPBRoot | awk '{print $NF}'`
SPBPrefix="202"
for item in $SPBList
do
    if [[ "$item" == "$SPBPrefix"* ]]; then
        SPBVersion=$item
    fi
done

echo $SPBVersion                                
