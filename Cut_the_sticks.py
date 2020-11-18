#!/bin/python

import sys


n = int(input().strip())
a = map(int,input().strip().split(' '))
while len(a) > 0:
    print len(a)
    m = min(a)
    l = []
    for i in a:
        j = i-m
        if j != 0:
            l += [j]
    a = l
