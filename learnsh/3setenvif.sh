#!/bin/sh
#set a env
export WYF=999
env > beforeunset.txt
if (grep WYF beforeunset.txt)
then 
    echo beforeunset yes
else
    echo beforeunset no
fi
# unset a env
unset WYF
env > afterunset.txt
if (grep WYF afterunset.txt)
then 
    echo afterunset yes
else 
    echo afterunset no
fi
