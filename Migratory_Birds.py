n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
m = 0
v = 0
for i in range(1,6):
    t = types.count(i)
    if t > m:
        v = i
        m = t
print(v)
