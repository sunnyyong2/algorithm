#바로 왼쪽의 숫자보다 큰 숫자의 갯수는?
#N개의 정수를 입력받아 정수로 리스트에 저장
N = int(input())
arr = list(map(int,input().split()))

cnt = 0
#탐색구간
for i in range(1, N):
    if(arr[i-1]<arr[i]):
       cnt = cnt + 1
print(cnt)

#바로 오른쪽의 숫자보다 큰 숫자의 갯수는?
#N개의 정수를 입력받아 정수로 리스트에 저장
N = int(input())
arr = list(map(int,input().split()))

cnt = 0
#탐색구간
for i in range(0,N-1):
    if(arr[i+1]<arr[i]):
        cnt = cnt + 1
print(cnt)

# Ai에 대해 왼쪽에서 가장 작은 수와의 차이(ㅣAi - minVㅣ)를 출력하는 프로그램을 만드시오. 1<=i<=N-1
N = int(input())
arr = list(map(int,input().split()))

#탐색구간1:처리할 원소의 범위
for i in range(1, N):
    #각 원소 Ai에 대해 할 일
    minV = arr[0]
    for j in range(1,i): #Ai의 왼쪽 구간에 대해
        if(minV>arr[j]):
            minV = arr[j]
    print(abs(arr[i]-minV), end=' ')
