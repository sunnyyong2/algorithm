T = int(input())

for i in range(1,T+1):
    tc = list(map(int,input().split()))
    M = 0
    for num in tc :
        if num > M :
             M = num

    print(M)




