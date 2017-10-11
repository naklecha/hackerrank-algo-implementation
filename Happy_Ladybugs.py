#!/bin/python3

import sys
from collections import Counter

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    #print(b)
    counts = Counter(b)
    #print (counts
    flag = False
    f = False;
    cntS = 0
    for k,v in counts.items():
        if(k != '_' and v == 1):
            print ("NO")
            flag = True
            break
        elif(k == '_'):
            cntS += 1
    
    if(cntS == n and flag == False):
        print("YES")
        flag = True
    elif(flag == False):
        if(cntS == 0):
            i = 0
            while(i<n-1):
                
                if(b[i] == b[i+1]):
                    while(i < n-1 and b[i] == b[i+1] ):
                        #print(i)
                        i += 1
                else: 
                    print("NO")
                    f = True
                    break
                i += 1
                
    if(flag == False and f == False):
        print("YES")
