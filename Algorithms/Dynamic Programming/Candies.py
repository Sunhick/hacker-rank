n = int(raw_input().strip())
mem = [1 for i in range(0, n)]
a = [int(raw_input().strip())]

for i in range(1, n):
    a.append(int(raw_input().strip()))
    mem[i] = 1+mem[i-1] if a[i] > a[i-1] else 1
    
for i in range(n-2, -1, -1):
    if a[i] > a[i+1]:
        mem[i] = max(mem[i], mem[i+1]+1)
        
print sum(mem)
