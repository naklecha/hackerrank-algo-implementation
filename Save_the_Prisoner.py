for i in range(input()):
    a,b,c = map(int, raw_input().split())
    d = (c + (b % a) - 1)%a
    if d > 0:
        print d
    else:
        print a
