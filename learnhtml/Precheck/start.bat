@echo off

(for /f "delims=" %%a in (temp.html) do (
set "str=%%a"
setlocal enabledelayedexpansion
set "str=!str:TestUser=%1%!"
set "str=!str:TestChange=%2%!"
set "str=!str:TestPort=%3%!"
echo !str!
endlocal
))>"start.html"

start "" start.html