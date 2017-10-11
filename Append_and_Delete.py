#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

lead = 0
for i in range(min(len(s),len(t))):
    if s[i] != t[i]:
        lead = i
        break
    else:
        lead = i + 1
        
d = len(s) - lead + len(t) - lead

if k >= len(s) + len(t):
    print("Yes")
elif d <= k and (d % 2) == (k % 2):
    print("Yes")
else:
    print("No")
