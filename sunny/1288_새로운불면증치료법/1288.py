import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # print(N)
    cnt = 0
    for i in range(N):
        cnt += i
