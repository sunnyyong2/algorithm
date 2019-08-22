N = int(input())
arr = [list(map(int,input().split())) for i in range(N)] # => 이차원 리스트
cnt = 0
for i in range(N): #행을 지정
    for j in range(N): #열을 지정
        if arr[i][j]%2==0: #짝수인 경우
            cnt += 1
print(cnt)
print(arr)

# 응용1; 짝수가 가장 맣은 행은?(0번행부터 시작)
# 응용2; 한 행에 최대 몇 개의 짝수가 존재하는가?
# 응용3; 짝수 중 가장 큰 값은?



### 연속된 1의 개수
1 1 1 1 0 0 1 1 0 1 1 0 1 1 1
1 1 1 1 (4)
  1 1 1 (3) -> 길이 4에 포함된 연속 1

# 방법 1
현재 위치에서 1이 시작되면
연속된 1의 개수를 확인
동시에 연속 구간에 포함되었음을 기록

# 방법 2
1) 현재 위치에서 1이 시작되면
2) 연속된 1의 개수를 확인.
3) 0이 나온 자리부터 새로운 1이 나올 때까지 이동

# 방법 3 -> 제일 심플
1) 1을 만날 때까지 이동
2) 1을 만나면 0을 만나거나 리스트가 끝날 때까지 이동하며 1의 개수를 셈
3) 1)을 반복
#조건에 의한 반복은 while이 제일 죠하

N,K = map(int,input().split())
arr = list(map(int,input().split()))

i  = 0 #탐색을 시작하는 위치
cntK = 0
while():
while(i<N and arr[i]==0): #0인 구간을 통과. arr[i]==1인 위치에서 빠져나옴
    i += 1
cnt = 0
while(i<N and arr[i]==1): #1인 구간을 이동. 1의 개수 카운트
    cnt += 1
    i += 1
if cnt == K:
    cntK += 1
print(cntK)

     15 3
     0 1 1 1 0 0 1 1 0 1 1 0 1 1 1
i    0 1 2 3 4 5 6 7
cnt  0 1 2 3 3 0 1 2   1 2 0 1 2 3
cntK       1       1             1
