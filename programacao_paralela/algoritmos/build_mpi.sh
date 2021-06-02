#!/bin/sh

FILE=$1
OUTNAME=$2
QTD_PROC=$3

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

if [ -z $QTD_PROC ]
then
    QTD_PROC="4"
fi

echo "Compiling $FILE \n"
mpicc $FILE  -o $OUTNAME && \
echo "Running $OUTNAME \n" && \
mpirun --hostfile mpi-hosts -np $QTD_PROC ./$OUTNAME


