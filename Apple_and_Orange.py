#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = len(list(filter(lambda x: int(x) + a <= t and int(x) + a >= s , input().strip().split(' '))))
orange = len(list(filter(lambda x: int(x) + b <= t and int(x) + b >= s , input().strip().split(' '))))
print(apple)
print(orange)
