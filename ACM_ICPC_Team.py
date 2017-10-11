#!/bin/python3

import itertools

N,M = map(int,input().strip().split())
knowledge=[]
for i in range(N):
    knowledge.append(int(input(),2))
mx = -float('inf')
teams=0
for p1,p2 in itertools.combinations(range(N),2):
    combined_topics = bin(knowledge[p1]|knowledge[p2]).count('1')
    if (combined_topics==mx):
        teams+=1
    elif (combined_topics>mx):
        mx = combined_topics
        teams=1

print(mx,teams,sep='\n')
