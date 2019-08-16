T = int(input())
for i in range(1,T+1):
    a,b = list(map(int,input().split()))
    m = a//b
    n = a % b
    print(m,n)