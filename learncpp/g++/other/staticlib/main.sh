#!/bin/sh

#build the static library libmath.a
g++ ./src/mymath.cpp -c -o ./lib/mymath.o -I ./include/

ar rcs ./lib/libmymath.a ./lib/mymath.o

#build main.cpp
# -I:the headers directory -L: the library directory -lmymath: libmymath.o
g++ main.cpp -I ./include -L ./lib -lmymath -o out