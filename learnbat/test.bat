call 1basic.bat
echo testtest1
echo %errorlevel%
call 1basic.bat
if "%errorlevel%"=="1" EXIT /B 1
echo testtest2