import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    board = []
    #sol1)
    #입력받은 데이터를 board로 만드는 작업
    for _ in range(N):
        text = input()
        board.append(list(text))

    #sol2)
    # board = [list(input()) for _ in range(N)]

    for row in range(N):
        for j in range(N-M+1):
            line = board[row][j:j + M]
            if line[::-1] == line:
                print(line)

    for col in zip(*board):
        for j in range(N-M+1):
            line = col[j:j + M]
            if line[::-1] == line:
                print(line)