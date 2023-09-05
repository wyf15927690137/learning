@echo off
echo test1
rem start C:\Users\yanfeiw\wyf\Nutstore\learning\learnbat 
set str1=This is a test string
echo %str1%
echo ---------------
echo %0
echo %~dp0
echo ---------------
echo test2
@REM cd wy
echo test3

@REM timeout 5

echo test4
echo %errorlevel%
fas
if "%errorlevel%" neq "0" EXIT /B 1
echo 11