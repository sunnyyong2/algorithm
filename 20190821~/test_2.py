T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    fly = [list(map(int, input().split())) for i in range(N)]

    # sol1)
    for i in range(0, N - K + 1):
        for j in range(0, M - k + 1):
            s = 0
            for p in range(K):
                s += arr[i][j + p]
                s += arr[i + K - 1][j + p]
                s += arr[i + p][j]
                s += arr[i + p][j + k - 1]
            s -= arr[i][j]
            s -= arr[i + K - 1][j]
            s -= arr[i][j + k - 1]
            s -= arr[i + k - 1][j + k - 1]
            if maxV < s:
                maxV = s
            for r in range(i, i + K):
                for c in range(j, j + K):
                    if r == i or r == i + K - 1 or c == j or c == j + K - 1:
                        s += arr[r][c]
            if maxV < s:
                maxV = s
    print()
