n = int(input())
s = input()
c = 0
tc = 0
for i in range(n):
    if(s[i]=="D"): c+=1
    else: c-= 1
    if(c==0 and s[i] == "U"): tc += 1
print(tc)
