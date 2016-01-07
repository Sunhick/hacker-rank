#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())

mapping = {
 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",15:"fifteen",20:"twenty",30:"thirty",40:"forty",50:"fifty"
}

if ( m == 0 ):
    print mapping[h] + " o' clock"
elif ( m == 30 ):
    print "half past " + mapping[h]
elif ( m == 15 ):
    print "quarter past " + mapping[h]
elif ( m <= 13 or m == 20 ):
    print mapping[m] + " minutes past " + mapping[h]
elif ( m > 13 and m < 20 ):
    print mapping[m-10] + "teen minutes past " + mapping[h]
elif ( m > 20 and m < 30 ):
    print "twenty " + mapping[m-20] + " minutes past " + mapping[h]
elif ( m == 40 or m == 50 ):
    print mapping[60-m] + " minutes to " + mapping[h+1]
elif ( m == 45 ):
    print "quarter to " + mapping[h+1]
elif ( m > 30 and m < 40 ):
    print "twenty " + mapping[40-m] + " minutes to " + mapping[h+1]
elif ( m > 40 and m < 47 ):
    print mapping[50-m] + "teen minutes to " + mapping[h+1]
elif ( m >= 47 and m < 60 ):
    print mapping[60-m] + " minutes to " + mapping[h+1]
