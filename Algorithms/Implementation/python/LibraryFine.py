import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

if ( y1 == y2 and m1 == m2 and d1 < d2 ):
    print "0"
elif( y1 == y2 and m1 == m2 and  d1 > d2  ):
    print (d1-d2)*15
elif( y1 == y2  and m1 > m2  ):
    print (m1-m2)*500
elif( y1 > y2 ):
    print "10000"
else:
    print "0"
