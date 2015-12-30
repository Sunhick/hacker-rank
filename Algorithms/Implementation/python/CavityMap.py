#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)


def checkIfChangeRequired(content,change):
    for x in change:
        content = content[0:x] + "X" + content[x+1:]
    print content
    #print type(content)
    
print grid[0]
for x in xrange(1,n-1):
    j = []
    for y in xrange(1,n-1):
        if ( grid[x-1][y] < grid[x][y] and grid[x+1][y] < grid[x][y] and grid[x][y-1] < grid[x][y] and grid[x][y+1] < grid[x][y] ):
            j.append(y)
    checkIfChangeRequired(grid[x],j)

if ( n > 1 ):
    print grid[n-1]
