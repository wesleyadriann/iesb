#!/bin/sh
echo "Deleting old version..."
rm *.out

FILE=$1
OUTNAME=$2

echo "Compile and run...\n"
gcc -o $OUTNAME.out $FILE -fopenmp && \
./$OUTNAME.out
