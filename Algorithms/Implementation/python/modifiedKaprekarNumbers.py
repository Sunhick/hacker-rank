import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
lowerRange = int(raw_input().strip())
upperRange = int(raw_input().strip())

finalNumbers = []
for x in xrange(lowerRange,upperRange+1):
    square = str( int(math.pow(x,2)))
    #print square
    #for y in xrange(len(square)):
    #print y , square[0:y] , square[y:len(square)]
    y = len(square)/2
    firstHalf = square[0:y]
    secondHalf = square[y:len(square)]
    #print "test" , firstHalf, "test1" ,secondHalf
    
    if ( firstHalf ):
        firstHalf = int(firstHalf)
    else:
        firstHalf = 0
    
    if ( secondHalf ):
        secondHalf = int(secondHalf)
    else:
        secondHalf = 0
    
    #if ( secondHalf != 0 ):
    total = firstHalf + secondHalf
    if ( total == x ):
        finalNumbers.append(x)

if ( finalNumbers ):
    #print finalNumbers
    print " ".join(map(str,finalNumbers))
else:
    print "INVALID RANGE"
