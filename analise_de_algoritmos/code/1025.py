
# -*- coding: utf-8 -*-

while True:
    x = input().split(' ')
    N = int(x[0])
    Q = int(x[1])
    if(not(N > 10000 or Q > 10000 or Q < 0 or N < 0)):
        numbers = []
        for i in range(N):
            numbers.append(int(input()))

        numbers.sort()
        for i in range(Q):
            try:
                x = int(input())
                y = numbers.index(x)
                print(x,'found at', y + 1)
            except ValueError:
                print(x,'not found')
    if(N == 0 and Q == 0):
        break
