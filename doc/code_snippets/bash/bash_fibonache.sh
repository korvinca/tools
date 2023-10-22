#!/bin/sh
#find . –mtime -2 –exec wc –l {} \;
a=1
b=1
echo $a
echo $b
L=(1 2 3 4 5 6 7 8)
for iterator in $L
do
c=a
b=$a
b=$(($a+$c))
echo $b
done