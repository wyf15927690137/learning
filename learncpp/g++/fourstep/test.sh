#!/bin/bash

echo complie process of test.cpp:
#preprocess
g++ -E test.cpp -o test.i
#compile
g++ -S test.i -o test.s
#assemble
g++ -c test.s -o test.o
#link
g++ test.o -o out
