#!/bin/python

import math


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
m = n+1
for i in xrange(n-1):
    for j in xrange(i+1,n):
        if A[i] == A[j] and m > math.fabs(i-j):
            m = math.fabs(i-j)
if m == n+1: print -1
else: print int(m)
            
