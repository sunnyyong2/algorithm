N = int(input())
N_1 = list(map(int,input().split()))
result = 1
most = 1
for i in range(1,N):
    if N_1[i-1] < N_1[i]:
        result += 1
        if most < result:
            most = result
    else:
        result = 1
print(most)

