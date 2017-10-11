# Enter your code here. Read input from STDIN. Print output to STDOUT

n, k = map(int, raw_input().split())
A = map(int, raw_input().split())
b = int(raw_input())

tot = sum(A) - A[k]
if 2*b == tot: print "Bon Appetit"
else: print b - tot / 2
