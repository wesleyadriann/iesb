
# -*- coding: utf-8 -*-

from time import time
from math import sqrt, pow
from sys import argv

def fibIte(n):
    x, y = 1, 1
    if n == 1:
        return x
    if n == 2:
        return y
    
    acc = 0
    for i in range(2, n):
        acc = x + y
        x = y
        y = acc
    return acc

def fibRec(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibRec(n-1) + fibRec(n-2)

def fibMath(n):
    sqrt5 = sqrt(5)
    return 1/sqrt5 * ( pow(((1 + sqrt5)/ 2), n) - pow(((1 - sqrt5)/ 2), n) )

N = 0
repeat = 10**7
mediaIte, mediaMath, mediaRec = [], [], []

def main():
    for i in range(1, 6):
        initialIte = time()
        for j in range(0, repeat):
            fibIte(N)
        totalIte = time() - initialIte
        mediaIte.append(totalIte)

        initialMath = time()
        for j in range(0, repeat):
            fibMath(N)
        totalMath = time() - initialMath
        mediaMath.append(totalMath)

        initialRec = time()
        fibRec(N)
        totalRec = time() - initialRec
        mediaRec.append(totalRec)
        print(f"""
        Execução {i}
        Tempo Iterativo : {totalIte} seg
        Tempo Matemativo: {totalMath} seg
        Tempo Recursivo : {totalRec} seg
        """)

    print(f"""
        n               : {N}
        Media Iterativo : {sum(mediaIte) / len(mediaIte)} seg
        Media Matematico: {sum(mediaMath) / len(mediaMath)} seg
        Media Recursivo : {sum(mediaRec) / len(mediaRec)} seg
    """)

if __name__ == "__main__":
    try:
        N = int(argv[1])
    except:
        N = 40
    
    main()