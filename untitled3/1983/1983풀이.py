import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,K = int,input().split()
    # print(N,K)
    mid,last,hk = list(map(int,input().split()))
    # print(mid,last,hk)
    score = ((mid*0.35)+(last*0.45)+(hk*0.2)/3)
    print(score)
