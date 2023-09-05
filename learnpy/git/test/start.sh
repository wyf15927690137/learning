#!/usr/bin/env bash

curScriptFolder=$(dirname "$(readlink -f "$0")")
export PATH=${curScriptFolder}/bin_linux/python3.7.12/bin:$PATH
export LD_LIBRARY_PATH=/grid/common/pkgs/gcc/v9.3.0p4/lib64:$LD_LIBRARY_PATH

python3 ${curScriptFolder}/start.py $@
