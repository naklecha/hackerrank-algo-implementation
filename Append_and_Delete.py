#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

l= 0
for i in range(min(len(s),len(t))):
    if s[i] != t[i]:
        l = i
        break
    else:
        l = i + 1
        
d = len(s) - l + len(t) - l

if k >= len(s) + len(t):
    print("Yes")
elif d <= k and (d % 2) == (k % 2):
    print("Yes")
else:
    print("No")
