# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    print(l.index(l.index(i+1)+1)+1)
