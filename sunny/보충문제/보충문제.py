import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
minV = 10000

for row in arr :
    if minV > sum(row):
        minV = sum(row)

for col in zip(*arr):
    if minV > sum(col):
        minV = sum(col)

print(minV)
