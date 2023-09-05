@echo off

(for /f "delims=" %%a in (ex.txt) do (
set "str=%%a"
setlocal enabledelayedexpansion
set "str=!str:line=line1!"
set "str=!str:river=river1!"
set "str=!str:sleep=sleep2!"
echo !str!
endlocal
))>"b.txt"

move /y "b.txt" "ex.txt"