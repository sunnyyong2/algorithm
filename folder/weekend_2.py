N = int(input())
N_1 = list(map(int,input().split()))

down = 0
count = 0
for i in range(1,N):
    if N_1[i-1] > N_1[i]:
        if down == 1:
            count += 1
            down = 0
    else:
        down = 1

print(count)