#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    #Chocolates for money
    moneyChocolates = n/c 
    #Chocolates from wrapper
    wrapperChocolates = (moneyChocolates/m)
    
    totalChocolates = moneyChocolates + wrapperChocolates
    
    #extraWrappers not used from initial money
    eWrapper = moneyChocolates%m
    #newWrappers from newly purchased chocolates
    eWrapperNew = wrapperChocolates
    
    totalWrapper = (eWrapper+eWrapperNew)
    while ( totalWrapper >= m ):
        totalChocolates += (totalWrapper)/m
        totalWrapper =  totalWrapper%m + (totalWrapper)/m

    print totalChocolates
