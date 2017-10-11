#!/bin/python3

import sys

def getWays(squares, d, m):
    c = 0
    for i in range(len(squares)-m+1):
        if d == sum(squares[i:i+m]):
            c+=1
    return c

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)
