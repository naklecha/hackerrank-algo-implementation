#!/bin/python

import sys


n = int(raw_input().strip())
p = int(raw_input().strip())
p = p/2 if p%2==0 else (p-1)/2
n = n/2 if n%2==0 else (n-1)/2
print(n-p if n-p<p else p)
