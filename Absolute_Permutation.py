t = int(raw_input())
ans = []

for _ in xrange(t):
    n,k = map(int,raw_input().split())
    ans = [0 for _ in xrange(n)]
    for i in xrange(1,n+1):
        if i-k >0 and ans[i-k-1]==0:
            ans[i-k-1] = i
        elif i+k <= n and ans[i+k-1] == 0:
            ans[i+k-1] = i
        else:
            break
    if 0 in ans:
        print -1
    else:
        print " ".join(map(str,ans))
