T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    weight = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    weight.sort() #오름차순 정렬
    truck.sort()
    #가장 무거운 컨테이너와 가장 큰 트럭을 가리키는 인덱스를 준비한다.
    #인덱스가 가리키는 컨테이너를 인덱스가 가리키는 트럭에
    #실을 수 있으면 두 인덱스를 다음으로 변경.
    #실을 수 없으면 컨테이너 인덱스만 다음으로 변경.
    idxW = N-1 #가장 무거운 화물
    idxT = M-1 #가장 큰 트럭
    total = 0
    while(idxT >= 0 and idxW >= 0): #트럭이 남아있는 동안
        if weight[idxW]<=truck[idxT]: #현재 가장 무거운 화물을 현재 가장 큰 트럭이 옮길 수 있으면
            total += weight[idxW]
            idxW -= 1
            idxT -= 1
        else: #옮길 수 없으면 해당 컨테이너는 포기하고 다음 컨테이너 선택
            idxW -= 1
    print('#{} {}'.format(tc, total))