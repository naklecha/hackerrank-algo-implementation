n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

ranking = [scores[0]]

for itm in scores:
    if itm != ranking[-1]:
        ranking.append(itm)

inx = len(ranking) - 1

for itm in alice:

    while itm > ranking[inx] and inx > -1:
        inx -= 1

    if itm == ranking[inx]:
        print (inx + 1)
    else:
        print (inx + 2)
