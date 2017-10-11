import sys

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = sorted(map(int,raw_input().strip().split(' ')))

last = 0
res = c[0]
for x in c:
    res = max(res, (x-last)/2)
    last = x
res = max(res, (n-1-last))
print res
