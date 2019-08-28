import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    print(a[N-1], a[0], a[N-2], a[1], a[N-3], a[2], a[N-4], a[3], a[N-5], a[4])



