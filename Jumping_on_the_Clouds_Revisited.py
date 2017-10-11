#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
ans = 99
if c[0] == 1:
    ans -= 2
i = k%n
while i != 0:
    ans -= 1
    if c[i] == 1:
        ans -= 2
    i = (i+k)%n
print ans
  
