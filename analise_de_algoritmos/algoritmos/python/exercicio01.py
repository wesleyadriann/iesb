
# -*- coding: utf-8 -*-

from random import random
from time import time
import sys

N = 1
X = 10
NMAX = N * (X**X)
frase = '-1'
sys.setrecursionlimit(NMAX)


# A - ITERATIVO
def iteSum(n):
    x = [random()]*n
    acc = 0
    for number in x:
        acc = acc + number

# A - RECURSIVO

def recSum(n ,i, numbers):
    try:
        return n + recSum(numbers[i], i + 1, numbers)
    except IndexError:
        return 0

# B - ITERATIVO
def itePrint(n):
    for x in range(0, n):
        print(frase)

# B - RECURSIVO
def recPrint(n, i):
    if i > n:
        return 0
    print(frase)
    recPrint(n, i + 1)


n = N
times = []
while (n < NMAX):
    n = n * 10
    numbers = [random()]*n
    inicial = time()
    inicialIteSum = time()
    for x in range(0, 10):
        iteSum(n)
    totalIteSum = inicialIteSum - time()
    initialRecSum = time()
    for x in range(0,10):
        recSum(0,0,numbers)
    totalRecSum = time() - initialRecSum
    initialItePrint = time()
    for x in range(0,10):
        itePrint(n)
    totalItePrint = time() - initialItePrint
    initialRecPrint = time()
    for x in range(0,10):
        recPrint(n, 0)
    totalRecPrint = initialRecPrint - time()
    totalTime = inicial - time()
    times.append(f"""
        | n           = {N}
        | iteSum      = {totalIteSum}
        | recSum      = {totalRecSum}
        | itePrint    = {totalItePrint}
        | recPrint    = {totalRecPrint}
        | total       = {totalTime}
    """)

print(''.join(times))

