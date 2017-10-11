#!/bin/python

import sys        

t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    chocs= n/c
    wrapper = chocs
    ex_chocs = wrapper/m
    while wrapper >= m:
        ex_chocs = wrapper / m
        wrapper = ex_chocs + wrapper % m
        chocs += ex_chocs
    print chocs

