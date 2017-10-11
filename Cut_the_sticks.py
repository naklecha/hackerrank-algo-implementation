#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while len(arr) > 0:
    print len(arr)
    m = min(arr)
    l = []
    for i in arr:
        j = i-m
        if j != 0:
            l += [j]
    arr = l
