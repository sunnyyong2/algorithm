import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1,T+1):
    moji = input()
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxV = 0
    S1 = 0
    S2 = 0

    for row in arr:
        if maxV < sum(row):
            maxV = sum(row)

    for col in zip(*arr):
        if maxV < sum(col):
            maxV = sum(col)

    for dia in range(N):
        S1 += arr[dia][dia]

    for rev_dia in range(N):
        S2 += arr[rev_dia][99-rev_dia]

    if maxV < S1:
        maxV = S1

    if maxV < S2:
        maxV = S2

    print(maxV)