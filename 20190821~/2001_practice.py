T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    fly = [list(map(int, input().split())) for i in range(N)]
    for i in range(0, N-k+1):
        maxV = 0
        for j in range(0, N-k+1):
            s = 0
            for r in range(i, i+K):
