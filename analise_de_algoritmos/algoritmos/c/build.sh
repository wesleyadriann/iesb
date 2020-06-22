#!/bin/sh
echo "Deleting old version...\n"
rm *.out

FILE=$1
OUTNAME=$2

echo "Compiling...\n"
gcc -o $OUTNAME.out $FILE -fopenmp -lm && \
echo "Running $OUTNAME.out ...\n" && \
./$OUTNAME.out
