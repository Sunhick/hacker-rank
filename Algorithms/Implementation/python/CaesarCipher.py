#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

s = list(s)

for x in xrange(0,n):
    if ( ord(s[x]) >=65 and ord(s[x]) <= 90 ):
        if ( ord( s[x] ) + k%26 <= 90 ):
            s[x] = chr( ord( s[x] ) + k%26 )
        else:
            s[x] = chr( ( ord( s[x] ) + k%26 )%90 + 64 )
    elif ( ord(s[x]) >=97 and ord(s[x]) <= 122 ):
        if ( ord( s[x] ) + k%26 <= 122 ):
            s[x] = chr( ord( s[x] ) + k%26 )
        else:
            s[x] = chr( ( ord( s[x] ) + k%26 )%122 + 96 )
    
    
    
s = ''.join(s)
print s
