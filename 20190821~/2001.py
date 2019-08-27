T = int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split())
    fly = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    for i in range(0, N-K+1): #부분 영역의 왼쪽 위 모서리칸 좌표, i, j
        for j in range(0, N-K+1):
            s = 0
            for m in range(K):
                s += fly[i + m][j + m]  # 오른쪽 아래 방향
                s += fly[i + m][j + K - 1 - m]  # 왼쪽 아래 방향
            # K가 홀수인 경우 가운데 원소가 두 번 더해지므로
            if K % 2 == 1:
                s -= fly[i + K // 2][j + K // 2]


            if maxV < s:
                maxV = s
    print('#{} {}'.format(tc,maxV))





for r in range(i, i + K):  # 영역 내부의 행 번호 i~i+K-1
    for c in range(j, j + K):  # 영역 내부의 열 번호
        s += fly[r][c]

        if K % 2 == 1:
            s -= fly[i+k//2][j+k//2]