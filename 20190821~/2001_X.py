(1) 파리채가 X 모양일 경우(크기는 K)
부분 배열의 왼쪽 위 모서리 좌표가 i,j일 때,
s = 0
for m in range(K):
        s += fly[i+m]{j+m} #오른쪽 아래 방향
        s += fly[i+m][j+k-1-m] #왼쪽 아래 방향
#K가 홀수인 경우 가운데 원소가 두 번 더해지므로
if K % 2 == 1:
    s -= fly[i+k//2][j+k//2] #한 개를 빼줌

(2) 파리채가 ㄱ, ㄴ, ㄷ, ㅁ 모양인 경우

(3)  파리채의 영역이 i+m, j+n일 때 (0<=m, n<K)
m이 짝수, n이 홀수
m이 홀수, n이 짝수
나머지는 구멍이 나서 파리가 죽지 않는다.