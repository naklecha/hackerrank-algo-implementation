
n,m = input().strip().split(' ')
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
c = 0
for i in range(max(a),min(b)+1):
    for j in a:
        if i%j!=0: break
    else:
        for k in b:
            if k % i != 0: break
        else: c+=1
print(c)
