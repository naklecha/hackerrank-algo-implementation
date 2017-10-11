#!/bin/python

h = int(raw_input().strip())
m = int(raw_input().strip())

d = dict(enumerate(['one', 'two', "three", "four", 'five', "six","seven","eight", "nine","ten","eleven","twelve", 'thirteen', 'fourteen'], 1))

if m == 0:
    print "{} o' clock".format(d[h])
elif m == 1:
    print "one minute past {}".format(d[h])
elif 1 < m < 15:
    print '{0} minutes past {1}'.format(d[m], d[h])
elif m == 15:
    print 'quarter past {}'.format(d[h])
elif 15 < m < 20:
    print '{0}teen minutes past {1}'.format(d[m-10], d[h])
elif m == 20:
    print 'twenty minutes past {}'.format(d[h])
elif 20 < m < 30:
    print 'twenty {0} minutes past {1}'.format(d[m-20], d[h])
elif m == 30:
    print 'half past {}'.format(d[h])
elif 30 < m < 40:
    print 'twenty {0} minutes to {1}'.format(d[40-m], d[h+1])
elif m == 40:
    print 'twenty minutes to {}'.format(d[h+1])
elif 40 < m < 45:
    print '{0}teen minutes to {1}'.format(d[h])
elif m == 45:
    print 'quarter to {}'.format(d[h+1])
elif 45 < m < 59:
    print '{0} minutes to {1}'.format(d[60-m], d[h+1])
elif m == 59:
    print "one minute to {}".format(d[h+1])
