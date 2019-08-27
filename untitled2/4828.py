T = int(input())
for i in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    MAX = max(ai)
    MIN = min(ai)
    print(MAX-MIN)
