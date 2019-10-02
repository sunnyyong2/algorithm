import sys
sys.stdin = open ('input.txt', 'r')

T = 10
for tc in range(1,T+1):
    moya = input()
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]
    minV = 99999
    minH = 999

    for h in range(1,30):
        for row in arr:
            value1 = 0
            for i in row:
                value1 += abs(i-h)
            if minV > value1:
                minV = value1
                minH = h

        for col in zip(*arr):
            value2 = 0
            for j in col:
                value2 += abs(j-h)
            if minV > value2:
                minV = value2
                minH = h

        value3 = 0
        for dia in range(N):
            value3 += abs(arr[dia][dia]-h)
        if minV > value3:
            minV = value3
            minH = h

        value4 = 0
        for rev_dia in range(N):
            value4 += abs(arr[rev_dia][99-rev_dia]-h)
        if minV > value4:
            minV = value4
            minH = h

    print("#{} {} {}".format(moya, minV, minH))
