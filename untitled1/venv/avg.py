T = int(input())
for i in range(1,T+1):
    tc = list(map(int,input().split()))
    average = sum(tc) / 10
    print(round(average))