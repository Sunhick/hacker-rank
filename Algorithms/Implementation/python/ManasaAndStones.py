import itertools
t = int(raw_input().strip())
for values in xrange(t):
    n = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())
    #print n,a,b
    #print list( itertools.combinations_with_replacement([a,b],n-1) )
    combinationsPossible = map(sum, itertools.combinations_with_replacement([a,b],n-1))
    print ' '.join(str(x) for x in sorted(list(set(combinationsPossible))))
