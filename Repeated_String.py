#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())
c = s.count('a')
c *= n//len(s)
q = n%len(s)
c += s[:q].count('a')
print (c)
