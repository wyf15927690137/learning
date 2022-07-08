set ProjectBuildPath=$1
if("$ProjectBuildPath" =~ */MFC/Projects/*) then
    echo "contains MFC Projects"
	setenv MSOFTLM_HOST @rmflex05
	setenv MWHOME "/lan/sig/cm/scratch/mainwin56/mw"
	source $MWHOME/setupmainwin.csh
	echo "set env successful"
else
    echo "Not contains  MFC Projects"
endif