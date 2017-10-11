# Enter your code here. Read input from STDIN. Print output to STDOUT

(N,K,Q) = tuple(map(int,raw_input().split(" ")))
a = map(int, raw_input().split(" "))
for q in xrange(Q):
    query = input()
    print a[(query - K) % N]
