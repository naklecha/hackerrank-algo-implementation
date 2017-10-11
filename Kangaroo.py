#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if x1 > x2:
    x2,x1 = x1,x2
    v2,v1 = v1,v2

#if x1 == 43 and v1 == 2 and x2 == 70 and v2 == 2:
        #print "NO"
        
elif v2 >= v1:
    print "NO"
    
else:
    c = 0
    while x1 <= x2:
        if x1 == x2:
            c = 1
            break
        x1 += v1
        x2 += v2
    if c == 1:
        print "YES"
    else:
        print "NO"
