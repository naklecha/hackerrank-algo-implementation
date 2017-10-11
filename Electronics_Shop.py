def getMoneySpent(ks, ds, s):
    su = 0
    for k in ks:
        for d in ds:
            if (su < k+d <=s):
                su = k + d
    if su: return su 
    else: return "-1" 
    
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
ks = list(map(int, input().strip().split(' ')))
ds = list(map(int, input().strip().split(' ')))
moneySpent = getMoneySpent(ks, ds, s) 
print (moneySpent)
