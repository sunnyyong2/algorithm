N = int(input())
factor = 0
for i in range(1,N+1):
    if N % i == 0:
        factor = i
        print(factor, end=' ')