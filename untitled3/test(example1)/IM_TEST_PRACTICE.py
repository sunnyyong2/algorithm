import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    AnswerN = 0
    N,M,K = list(map(int, input().split()))
    # DRAW = [[int(num) for num in input().split()] for _ in range(K)]
    grid = [[0]*M for _ in range(N)]
    for _ in range(N):
        x1, y1, x2, y2, color = list(map(int, input().split()))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                this_color = grid[i][j]
            if this_color == 0 :
                AnswerN += 1
                print(AnswerN)
            # else:
            #     if this_color != color:

        # for i in range(N,M):
        #     for j in range(N,M):
        #         DRAW[i][j] = grid[i][j]
        # print(DRAW)
    for _ in range(M):