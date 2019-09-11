import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = [list(map(int,input().split()))]
    sudoku = [[]]
    I = []
    for i in range(9):
        I += str(i)
print(len(I))


