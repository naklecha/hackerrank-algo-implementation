#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
ObList = []
for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    # your code goes here
    ObList.append((rObstacle,cObstacle))
ObSet = set(ObList)
Delta = [(0,1),(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(1,-1),(-1,1)]
Count = 0
for shift in Delta:
    Pos = (rQueen,cQueen)
    while Pos[0] + shift[0] >=1 and Pos[0] + shift[0] <= n and Pos[1] + shift[1] >=1 and Pos[1] + shift[1] <= n:
        Pos = (Pos[0]+shift[0],Pos[1]+shift[1])
        if Pos in ObSet:
            break
        Count += 1
print(Count)
            
