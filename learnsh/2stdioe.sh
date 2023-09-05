#!/bin/sh
sh 1echo.sh > stdout.txt
sh 1echo.sh > stdoe.txt 2>&1
sh 1echo.sh 2>&1 | tee stdoeTee.log