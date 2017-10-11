#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
cnt = [0]*k
for x in a:
    cnt[x % k] += 1
i, j, r = 1, k-1, 0
if cnt[0] > 0:
    r += 1
while i < j:
    r += max(cnt[i],cnt[j])
    i, j = i+1, j-1
if i == j and cnt[i] > 0:
    r += 1
print r
