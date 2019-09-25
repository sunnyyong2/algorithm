import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

minV = 10000
h = 0
for num in range(1, M + 1):
    s = 0
    for i in range(N):
        for j in range(N):
            s += abs(num - arr[i][j])
    print('{}로 만들때 최소비용: {}'.format(num, s))
    if minV > s:
        minV = s
        h = num
print(h, minV)