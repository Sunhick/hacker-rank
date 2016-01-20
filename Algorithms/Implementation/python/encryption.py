#!/bin/python

import sys
import math


s = raw_input().strip()
column = int ( math.ceil( math.sqrt(len(s)) ) )
row = int ( math.floor( math.sqrt(len(s)) ) )
while ( row * column < len(s) ) :
    if(column + 1 < math.sqrt(len(s))):
        column += 1 ;
    else:
        row += 1;
        
output = {} 
for i in xrange(0,row):
    for j in xrange(0,column):
            if ( len(output) < len(s) ):
                output[i,j] = s[len(output)];
            else:
                output[i,j] = "";

getFromOutput = ""
for i in xrange(0,column):
    for j in xrange(0,row):
            getFromOutput += output[j,i];
    getFromOutput += " " ;   
print getFromOutput
        
