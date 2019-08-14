N = list(map(int,input().split()))
num = 0
    if (a % 2 ==0):
        num += 1
    else:
        pass

*** 쓰앵님 ***

#N개의 정수를 입력받아 정수로 리스트에 저장
N = int(input())
arr = list(map(int,input().split()))

cnt = 0
for i in range(0,N): #탐색 구간. 0부터 N개
    if(arr[i] % 2 ==0): #각 숫자에 대해(리스트의 각 원소에 대해)
        cnt = cnt + 1
print(cnt)

# + N과 M이 주어진다. N개의 정수가 입력될 때마다 M보다 큰 수의 갯수를 출력하시오.
N,M = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
for i in range(0,N):
    if (arr[i] > M):
        cnt = cnt + 1
print(cnt)

# + N과 N개의 정수가 한 줄에 입력된다. N개의 정수 중 홀수의 갯수를 출력하시오.
arr = list(map(int,input().split()))
N = arr[0]
cnt = 0
for i in range(1,N+1): #탐색구간
#for i in range(1,arr[0]+1):
    if(arr[i] % 2 == 1):
        cnt = cnt + 1
print(cnt)
