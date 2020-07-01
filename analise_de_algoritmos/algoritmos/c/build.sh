#!/bin/sh

echo "
##########################################
#                 author                 #
#             Wesley Adriann             #
#                 github                 #
#    https://github.com/wesleyadriann    #
##########################################
"

echo "Deleting old version\n"
rm *.out

FILE=$1
OUTNAME=$2

if [ -z $FILE ]
then
    echo "File to compile is missing"
    echo "./build.sh filename.c\n"
    exit
fi

if [ -z $OUTNAME ]
then
    OUTNAME="a"
fi

echo "Compiling $FILE \n"
gcc -o $OUTNAME.out $FILE -fopenmp -lm && \
echo "Running $OUTNAME.out \n" && \
./$OUTNAME.out
