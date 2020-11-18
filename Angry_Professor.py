#!/bin/python

import sys


t = int(input().strip())
for a0 in xrange(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,input().strip().split(' '))
    s = 0
    for i in a:
        if i <= 0:
            s += 1
    if s <= k:
        print("YES")
    else:
        print("NO")
