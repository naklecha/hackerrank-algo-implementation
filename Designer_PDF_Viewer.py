h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()
l = max([h[ord(i)-97] for i in word])
print(l*len(word))
