# Enter your code here. Read input from STDIN. Print output to STDOUT

p=int(input())
q=int(input())
flag = True
for i in range(p,q+1):
    sq = i*i
    s=str(sq)
    if sq < 10:
        s = '0'+s
    l = s[0:int(len(s)/2)]
    r = s[int(len(s)/2):]
    if int(l)+int(r) == i:
        print (i , end = ' ')
        flag = False
if flag:
    print ("INVALID RANGE")
