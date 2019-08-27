import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [[0] * N for _ in range(N)]
    black_count = 0
    for _ in range(M):
        x1, y1, x2, y2 = list(map(int, input().split()))
        for i in range(x1 - 1, x2):
            for j in range(y1 - 1, y2):
                # point = grid[i][j]
                grid[i][j] = 1

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                black_count += 1
    print(black_count)