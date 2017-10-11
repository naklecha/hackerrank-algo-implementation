#!/bin/python

import sys


N = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
#1 if bad
memo = {}
def dp(x):
    #min from x
    if x == N-1: return 0
    if x >= N: return 10000000
    if x in memo: return memo[x]
    ans = 1000000
    if not A[x+1]: ans = 1+min(ans, dp(x+1))
    if x+2 < N and not A[x+2]: ans = 1+min(ans,dp(x+2))
    memo[x] = ans
    return ans
print dp(0)
