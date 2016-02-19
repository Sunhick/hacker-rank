def fib(lut, N):
    for i in range(2, N):
        lut.append(lut[i-1]**2 + lut[i-2])
    return lut[N-1]

if __name__ == '__main__':
    a, b, N = [int(v) for v in raw_input().strip().split(' ')]
    lut = [a, b]
    print fib(lut, N)
