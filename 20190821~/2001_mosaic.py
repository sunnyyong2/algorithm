#부분 배열의 왼쪽 위 모서리 (i,j)
#부분 배열의 크기 K=3일때
#[]칸은 유효하다면

(i,j)       [i,j+1]     (i,j+2)
[i+1,j]     (i+1,j+1)   [i+1, j+2]
(i+2,j)     [i+2,j+1]   (i+2,j+2)

for i in range(0,N-K+1):
    for j in range(0,N-K+1):
        s = 0
        for m in range(K):
            for n in range(K):
                if m%2!= n%2 : #m과 n이 각각 짝수와 홀수면 유효
                    s += arr[i+m][j+n]
            if maxV<s:
                maxV=s