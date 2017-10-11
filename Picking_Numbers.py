from collections import Counter

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
counter = Counter(a)
keys = list(counter.keys())
print(max([counter[keys[i]] + counter[keys[i+1]] for i in range(len(keys)-1) if keys[i+1]-keys[i]==1] +list(counter.values())))
