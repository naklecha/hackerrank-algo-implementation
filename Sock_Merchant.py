n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
b = set(c)
co = 0
for i in b:
    co += c.count(i)//2
print (co)
