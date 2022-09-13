#!/bin/csh
echo "this is csh"

if ( "true" == "true" ) then
    echo "success"
    # set exit code as $?, if last command executes successfully, then $? == 0, and then the current script will be exited.
    exit $?
else
    echo "fail"
    ./code.sh
    exit $?
endif
exit $?