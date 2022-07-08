#!/bin/csh
set x=6
set y=6
set z=9
if ($x == $y) then
   echo foo!
else if ($y=$z) then
    echo del!
else
   echo bar!
endif
endif