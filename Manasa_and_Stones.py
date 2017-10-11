# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())
for _ in range(T):
    N = input()
    a = input()
    b = input()

    val = set([0])
    for i in range(2,N+1):
        val = set([x + a for x in val]) | set([x + b for x in val])
    print ' '.join(map(str, sorted(val)))
