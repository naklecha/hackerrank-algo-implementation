import sys


N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

ans = 0

for i in xrange(N-1):
    if B[i]%2 == 1:
        B[i] += 1
        B[i+1] += 1
        ans += 2
        
if B[N-1] % 2 == 1:
    print "NO"
else:
    print ans
  
