T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #기지국과 짐 정보 입력
    arr = [list(input()) for _ in range(N)]
    #arr = [input() for _ in range(N)]
    #기지국 찾기
    arr[2][3] = 'Y'
    print(arr[2][3])
    #남은 집 개수 세기