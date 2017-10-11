#!/bin/python

import math

s = raw_input().strip().replace(' ', '')
cols = int(math.ceil(len(s) ** 0.5))

for i in range(cols):
    print ''.join([s[x] for x in range(i, len(s), cols)]),
