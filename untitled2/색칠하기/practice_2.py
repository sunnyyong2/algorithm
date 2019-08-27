import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [[0]*10 for _ in range(10)]
    purple_count = 0
    for _ in range(N):
        r1,c1,r2,c2,color = list(map(int,input().split()))

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                this_color = grid[i][j]
                if this_color == 0:
                    grid[i][j] = color
                else:
                    if this_color != color:
                        grid[i][j] = 'p'
                        purple_count += 1
    print(purple_count)
