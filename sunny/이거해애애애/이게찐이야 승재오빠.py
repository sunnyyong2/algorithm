import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    cross = [list(map(int, input().split())) for _ in range(100)]
    minreal = 9999999
    heigh = 999
    for h in range(1, 30):
        mintmp = 99999
        row = 0
        col = 0
        left = 0
        right = 0
        for t in range(100):
            left += abs(h - cross[t][t])
            right += abs(h - cross[t][99-t])
        for i in range(100):
            for j in range(100):
                row += abs(h - cross[i][j])
                col += abs(h - cross[j][i])
            tt = min(row, col, left, right)
            row = 0
            col = 0
            if mintmp > tt:
                mintmp = tt
        if minreal > mintmp:
            minreal = mintmp
            heigh = h
    print("#{} {} {}".format(tc+1, minreal, heigh))