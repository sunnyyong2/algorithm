N = int(input())

count = 1
for i in range(1,N+1):
    N_1 = list(map(int, input().split()))

    if i % 2 != 1:
        count += 1
    print(count)
