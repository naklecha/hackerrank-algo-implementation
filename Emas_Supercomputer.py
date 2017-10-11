#!/bin/python
import sys
from copy import deepcopy
n,m = map(int,raw_input().strip().split())
a = [list(raw_input().strip()) for i in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if a[i][j]=='B':
            continue
        a1=deepcopy(a)
        ct=1
        a1[i][j]='B'
        while j+ct<m and j-ct>=0 and a1[i][j+ct]=='G' and a1[i][j-ct]=='G' and i+ct<n and i-ct>=0 and a1[i+ct][j]=='G' and a1[i-ct][j]=='G':
            a1[i][j+ct]='B'
            a1[i][j-ct]='B'
            a1[i+ct][j]='B'
            a1[i-ct][j]='B'
            ct+=1
        ct-=1
        ctt=-1
        for x in range(n):
            for y in range(m):
                if a1[x][y]=='B':
                    continue
                pt=1
                while y+pt<m and y-pt>=0 and a1[x][y+pt]=='G' and a1[x][y-pt]=='G' and x+pt<n and x-pt>=0 and a1[x+pt][y]=='G' and a1[x-pt][y]=='G':
                    pt+=1
                pt-=1
                ctt=max(ctt,pt)
        if ctt>=0:
            ans=max(ans,(4*ct+1)*(4*ctt+1))
print ans
