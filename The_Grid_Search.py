# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(R, C, G, r, c, P):
    for i in xrange(R-r+1):
        for j in xrange(C-c+1):
            found = True
            for k in xrange(r):
                if P[k] != G[i+k][j:j+c]:
                    found = False
                    break
            if found:
                return "YES"
    return "NO"
            
T = int(raw_input())
for _ in xrange(T):
    R, C = (int(x) for x in raw_input().strip().split())
    G = [raw_input().strip() for i in xrange(R)]
    
    r, c = (int(x) for x in raw_input().strip().split())
    P = [raw_input().strip() for i in xrange(r)]
    
    print solve(R, C, G, r, c, P)
