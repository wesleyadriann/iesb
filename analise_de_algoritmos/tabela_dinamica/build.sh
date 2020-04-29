#!/bin/sh
echo "Deleting old version..."
rm *.out

FILE=$0
OUTNAME=$1

echo "Compile and run...\n"
gcc -o tabela.out tabela_dinamica.c && \
./tabela.out