import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tri = [[0] * N for _ in range(N)]
    # print(tri)
    # for i in range(N):
        # tri[2][1] = tri[1][0] + tri[1][1]
    # print(tri[2][1])
    # tri[i][i-1] = tri[i-1][i-1] + tri[i-1][i-2]
    # print(tri[i][i-1])
    for i in range(N):
        for j in range(N):
            if j == 0 or j == i:
                tri[i][j] = 1
            else:
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
            if tri[i][j] != 0:
                print(tri[i][j], end=' ')
        print()
