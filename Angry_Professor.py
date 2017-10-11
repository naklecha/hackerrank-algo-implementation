#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    s = 0
    for i in a:
        if i <= 0:
            s += 1
    if s >= k:
        print "NO"
    else:
        print "YES"
