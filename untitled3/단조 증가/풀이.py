T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = list(map(int, input().split()))
    maxV = -1
    for i in range(N-1):
        for j in range(i+1,N):
            m = A[i]*A[j]
            s = str(m)
            for k in range(1,len(s)):
                if(s[k-1]<=s[k]):
                    if(k==(len(s)-1) and maxV<M):
                        maxV = m
                else:
                    break
    print('# {} {}'.format(tc.maxV))

    #KEYPOINT
    #곱할 숫자 두 개를 뽑아내고
    #이 숫자 두 개를 확인