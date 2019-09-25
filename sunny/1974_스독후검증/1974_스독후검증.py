import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
arr = [list(map(int,input().split())) for _ in range(T)]
LIST = []

for i in arr:
    LIST += i
for j in zip(*arr):
