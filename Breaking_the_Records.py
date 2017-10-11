#!/bin/python3

import sys

def getRecord(s):
    mi = ma = s[0]
    mic = mac = 0
    for i in range(len(s)):
        if s[i] > ma:
            ma = s[i] 
            mac += 1
        if s[i] < mi:
            mi = s[i] 
            mic += 1
    return [mac,mic]
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
