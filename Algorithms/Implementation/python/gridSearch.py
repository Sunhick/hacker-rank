#!/bin/python

import sys
import re


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1
        
t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
   
    FOUND="NO"
    i = 0
    while (i < R):
        #test = G[i].find(P[0])
        test = list(find_all(G[i],P[0]))
        currentIndexMatched = test
        #print currentIndexMatched
        if ( test == -1 ):
            i += 1
        else:
            j = 0
            k = i
            while ( j < r and test == currentIndexMatched ):     
                if ( k < R ):
                    #test = G[k].find(P[j])
                    test = list(find_all(G[k],P[j]))
                    currentIndexMatched = [val for val in test if val in currentIndexMatched]
                    test = [val for val in test if val in currentIndexMatched]
                    if ( currentIndexMatched == []):
		                break
		    
		    #print G[k] , P[j] , test , currentIndexMatched
                    if ( currentIndexMatched == test ):
                        j += 1
                        k += 1
                else:
                    break
                
            if ( j == r and test != -1 and currentIndexMatched != [] ):
                #print "Hello" , j , test
                FOUND="YES"
            i += 1
            
    print FOUND
              
