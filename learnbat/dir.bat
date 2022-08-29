@echo off 
set CurDir=%~dp0
echo %PATH% | findstr "Git">nul 
if "%errorlevel%" == "0" (echo "git has been added to path"
) else (set gittool=%CurDir%\bin\PortableGit\bin
)
if exist %gittool% set PATH=%PATH%;%gittool%
git --version