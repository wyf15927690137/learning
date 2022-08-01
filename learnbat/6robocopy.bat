@REM copy files from ./Test1  to ./Test2
@echo off
robocopy /S ./Test1 ./Test2 /MIR /NDL
robocopy /S ./Test1 ./Test2 /MIR /NDL


if(%errorlevel% LSS 3) (
    echo "errorlevel is %errorlevel%, and set it as 0"
    echo %errorlevel%
    ) else  ( echo "There is error when copy")

@REM robocopy folder1 folder2 /S /move