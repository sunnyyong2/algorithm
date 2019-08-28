(1) 충전기 위치만 저장. 마지막으로 충전한 충전기에서 최대로 이동할 수 있는 충전기(반드시 지나쳐야 할 정류장 번호)를 찾는 방식
(출발지는 충전기가 있고, 종점은 충전기는 아니지만 종점까지 갈 수 있는지 확인하기 위한 용도)
[0, 1, 3 ,5, 7, 9, 10]

1) stop[i] - stop[i-1] <= K
(두 충전기 사이 간격이 최대 이동거리 이내여야 함)
만약 stop[i] - stop[i-1] > K인 상황이면 운행 중단

T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int, input().split())
    stop = [0] + list(map(int, input().split())) + [N]
    last = 0
    for i in range(1,M+2):
        if stop[i]-stop[i-1]: #두 충전기 거리가 K보다 크면 중단
            break
        else:
            if stop[i] - stop[last]>K: #i번 충전기에 도착할 수 없으면
                last = i -1 # 하나 전 충전기에서 충전하고
                cnt += 1 #충전횟수 증가
    if result == 0:
        print('#{} 0'.format(tc,0))
    else:
        print('#{} 0'.format(tc,cnt))

2) 마지막 충전 인덱스를 last라 하고,
stop[i] - stop[last] > K 마지막 충전 위치에서 갈 수 없는 인덱스 i에 다다르면, 이전 충전기에서 충전.(last = i-1,)
(도착할 수 있는 충전기는 통과해서 다음 충전기로 가봄. 도착할 수 없는 충전기면 바로 이전에 통과한 충전기에서 충전)