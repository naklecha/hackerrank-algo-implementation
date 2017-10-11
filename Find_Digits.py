#!/bin/python

import sys

def check(a):
    s = 0
    for i in str(a):
        i = int(i)
        if i != 0 and a % i == 0:
            s = s + 1
    return s

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print check(n)
