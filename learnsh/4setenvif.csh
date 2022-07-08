#!/bin/csh

# input csh in terminal, enter into cshell

#set a env
setenv LLD 888
env > beforeunset_csh.txt

#grep will return 0 or 1
if ($SHELL==$SHELL) then
    echo beforeunset yes
else 
    echo beforeunset no
endif
endif
#unset a env
# unsetenv LLD

# env > afterunset_csh.txt
# if (grep LLD afterunset_csh.txt) then 
#     echo afterunset yes
# else
#     echo afterunset no
# endif
