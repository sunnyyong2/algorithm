import sys
sys.stdin = open('input.txt', 'r')
#인풋을 잘받자!!!!111
T = 10 #테스트케이스 갯수
for tc in range(1,T+1): #테스트케이스 한 개씩 돌리자
    moji = input() #의미없는 인풋값. 얘는 마지막에 프린트할 때만 사용할거야
    N = 100 #100*100의 정사각형이니까
    arr = [list(map(int,input().split())) for _ in range(N)] #이차원리스트 만들자
    minV = 99999 #최소비용
    minH = 999 #밀린 땅 높이
    # height = 0

    for h in range(1,30): #이차원리스트의 수 범위가 1부터 30까지
        for row in arr: #열 한 개씩
            value1 = 0 #최소비용 임시저장소 밸류1 위치 중요해! row와 i 두 개의 포문 사이에 있는겨
            for i in row: #열의 한 원소(?)
                value1 += abs(i-h) #열의 한 원소에서 h값을 뺀 절대값을 value1에 더해쥼
            if minV > value1: #만약 minV가 value1보다 크면 #if 인덴트 중요해! for랑 같은 인덴트
                minV = value1 #value1을 minV에 할당
                minH = h #h를 minH에 할당해서 판판한 땅 높이를 구해
        for col in zip(*arr): #행 한 개씩
            value2 = 0 #최소비용 임시저장소 밸류2 위치 중요해! row와 i 두 개의 포문 사이에 있는겨
            for j in col: #행의 한 원소(?)
                value2 += abs(j-h) #행의 한 원소에서 h값을 뺀 절대값을 value2에 더해쥼
            if minV > value2: #만약 minV가 value2보다 크면 #if 인덴트 중요해! for랑 같은 인덴트
                minV = value2 #value2을 minV에 할당
                minH = h #h를 minH에 할당해서 판판한 땅 높이를 구해
        value3 = 0 #얘가 포문 안으로 들어가면 0으로 계속 초기화
        for dia in range(N): #왼쪽에서 시작하는 대각선 한 개씩 뽑앙보쟈 range(N) 주의
            value3 += abs(arr[dia][dia]-h) #value3에 대각선좌표(가로세로 인덱스 똑같음)에서 h뺀거 절대값을 더해
        if minV > value3: #만약 minV가 value3보다 크면
            minV = value3 #value3을 minV에 할당
            minH = h #h를 minH에 할당해서 판판한 땅 높이를 구해
        value4 = 0 #얘가 포문 안으로 들어가면 0으로 계속 초기화
        for rev_dia in range(N): #오른쪽에서 시작하는 대각선 한 개씩 뽑아보자 range(N) 주의주의
            value4 += abs(arr[rev_dia][99-rev_dia]-h) #value4에 오른쪽에서 시작하는 대각선좌표(99 주의)에서 h뺀거 절대값을 더해
        if minV > value4: #만약 minV가 value4보다 크묜
            minV = value4 #value4를 minV에 할당
            minH = h #h를 minH에 할당해서 판판한 땅 높이를 구해
    print("{}, {}".format(minV,minH))