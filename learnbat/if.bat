@echo off
set x=%1
set y=%2
IF %x% EQU %y% (echo yes) ELSE (echo no)
set item1=abc
set item2=xyz
IF NOT %item1% == %item2% (echo yes
) ELSE (echo no)


if not exist F:\\ (echo no) else (echo yes)
set INS=
if defined INS (echo yes) else (echo no)

if exist J:\\ (echo "J:\\ already exsited!"
) else (tzutil /g | findstr "China" >nul && (net use J: \\shwinshare\wint$) || (net use J: \\sjvclapa02-p9\sigrity_fort04\sigrity\publish\cdsnt))
set CDS_INST_DIR=J:/22.10/main/latest

cd C:\ &&(echo yes)||(echo no)
echo "-----------------------"

findstr "basic" ./test.bat &&(echo yes)||(echo no)
echo "-----------------------"
findstr "basic" ./test.bat > nul &&(echo yes)||(echo no)
echo "-----------------------"
findstr "basif" ./test.bat &&(echo yes)||(echo no)