def StockMaximize(arr):
    p=0
    m=0
    for i in range(len(arr)-1,-1,-1):
        v=arr[i]
        if m<=v:
            m=v
            p+=m-v
    return p

t = int(raw_input().strip())
for i in range(0, t):
    n = int(raw_input().strip())
    arr = [int(a) for a in raw_input().strip().split(' ')]
    print StockMaximize(arr)
