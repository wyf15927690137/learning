@echo off
set str=machine-order-service
set matchStr=order
@REM not show the output of a command
@REM > nul

echo "abc" 
echo "abc" > nul
echo "-----------------------"

echo %str% | findstr %matchStr% >nul && echo yes || echo no

@REM tzuitl /g : get time zone
@REM command1 && command2 : command2 will be executed only when command1 successfully executed
@REM command1 || command2 : command2 will be executed only when command1 failed to execute
tzutil /g | findstr "China" >nul && (echo yes) || (echo no)


set str1=abc
set str2=abc123
@REM findstr will return the whole line which contains the found content
@REM find str1 in str2
echo %str2% | findstr %str1%
echo "-----------------------"
echo "wy" | findstr "w"
echo "-----------------------"