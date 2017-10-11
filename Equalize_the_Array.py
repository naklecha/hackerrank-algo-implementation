from collections import Counter

n, a = int(input()), list(map(int, input().split()))
print(min(n - cnt for x, cnt in Counter(a).items()))
