import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
S1 = 10000
S2 = 10000

for row in arr:
    S1 = sum(row)
    for col in zip(*arr):
        S2 = sum(col)

#인덱스를 써서 중복값 제거?
print(S2)