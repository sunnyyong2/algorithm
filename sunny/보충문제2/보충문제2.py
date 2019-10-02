import sys
sys.stdin = open('input.txt', 'r')

T = 2 #테스트케이스 갯수
for tc in range(1,T+1): #테스트케이스를 for문으로 돌리자
    moji = input() #당장은 필요없는 값. 프린트할 때 테스트케이스 갯수 셀 때만 필요
    N = 100 #100*100인 정사각형
    arr = [list(map(int,input().split())) for _ in range(N)] #인풋받아서 배열만들기
    minV = 99999
    minH = 999

    for h in range(1,30):
        for i in range(N):
            row = arr[i]
            for col in zip(*arr):
                S = 0
                for z in range(N):
                    S += abs(row[z]-h)
                    S += abs(col[z]-h)
                S -= abs(col[i]-h)
                if minV > S:
                    minV = S
                    minH = h
    print(minV, minH)