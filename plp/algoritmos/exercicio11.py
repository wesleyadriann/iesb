
# -*- coding: utf-8 -*-

from multiprocessing import Pool
from time import time

def valida_primo(numero = 0):
    for i in range(2, numero):
        if(numero % i == 0):
            return
    print(f'{numero} ')

def main():
    pool = Pool(10)
    for i in range(0, 100000, 10000):
        pool.map(valida_primo, list(range(i,i + 10000 - 1)))

if __name__ == '__main__':
    main()
