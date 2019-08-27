import sys

sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트케이스 개수

for tc in range(1, T + 1):

    N = int(input())  # 칠하는 횟수

    grid = [[0] * 10 for _ in range(10)]  # 칠할 판떼기를 만든다.

    purple_count = 0

    # 칠하는 횟수만큼 어떻게 칠하는지 받는다

    for _ in range(N):
        # 칠할 정보를 얻었다.
        x1, y1, x2, y2, color = list(map(int, input().split()))


        # 1.얻은 정보를 토대로 grid에 색을 칠한다.
        # left_top = grid[x1][y1]
        # right_bottom =grid[x2][y2]

        # 2.원하는 영역에 접근한다.

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 구한 영역에 색을 칠한다
                this_color = grid[i][j]

                # 아직 아무것도 안칠해져 있을때
                if this_color == 0:
                    # 그냥 칠함
                    grid[i][j] = color

                # 뭔가 칠해져있을때
                else:
                    if this_color != color:
                        grid[i][j] = 'p'
                        purple_count += 1

    print(purple_count)
