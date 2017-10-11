# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
l = map(int,raw_input().split())
sl = sorted(l)

diffcount = 0
diff1 = -1
diff2 = -1

for i in range(len(l)):
    if sl[i] != l[i]:
        diffcount += 1
        if diff1 == -1:
            diff1 = i
        elif diffcount > 1:
            diff2 = i
        lastdiff = i
        
if diffcount == 2:
    l[diff1], l[diff2] = l[diff2], l[diff1]
    if l == sl:
        print "yes"
        print "swap {} {}".format(diff1+1, diff2+1)
    else:
        print "no"
elif diffcount > 2:
    l = l[:diff1] + l[diff1:diff2+1][::-1] + l[diff2+1:]
    if l == sl:
        print "yes"
        print "reverse {} {}".format(diff1+1, diff2+1)
    else:
        print "no"
elif l == sl:
    print "yes"
