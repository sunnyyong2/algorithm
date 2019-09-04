N = int(input())
for i in range(1,N+1):
    if N%i == 0:
        print(f'{i}(은)는 5의 약수입니다.)
        if i ==  1 and N:
            print(f'{i}(은)는 1과 5로만 나눌 수 있는 소수입니다.)