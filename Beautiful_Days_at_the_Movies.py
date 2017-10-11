i, j, k = [int(x) for x in input().split()]
s = 0
for day in range(i, j+1):
    if (day - int(str(day)[::-1])) % k == 0:
        s += 1
print(s)
