import sys
sys.stdin = open('input.txt', 'r')

T = 2
for tc in range(1,T+1):
    moji = input()
    M, N = 100, 10
    arr = [list(map(int,input().split())) for _ in range(N)]
    minV = 99999
    minH = 999

    for h in range(1,30):
        for i in range(N):
            row = arr[i]
            for col in zip(*arr):
                S = 0
                for z in range(M):
                    S += abs(row[z]-h)
                    S += abs(col[z]-h)
                S -= abs(col[i]-h)

                if minV > S:
                    minV = S
                    minH = h
    print('#{} {} {}'.format(moji, minV, minH))