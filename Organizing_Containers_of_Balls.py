q = int(input().strip())

for x in range(q):
    
    n = int(input().strip())
    m = []
    rowsum = [0]*n
    colsum = [0]*n
    
    for i in range(n):
        m.append(list(map(int,input().strip().split(' '))))
        rowsum[i] = sum(m[-1])
        colsum = list(map(lambda a, b: a+b, colsum, m[-1]))
        
    rowsum.sort()
    colsum.sort()
    
    if rowsum == colsum:
        print('Possible')
    else:
        print('Impossible')
