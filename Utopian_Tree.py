#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    h = 1
    c = 1
    for i in range(n):
        if c == 1:
            h = h * 2
        else:
            h = h + 1
        c *= -1
    print h
