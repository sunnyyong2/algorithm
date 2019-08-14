N = int(input())
score = list(map(int, input().split()))
score.sort()
idx = len(score) // 2
print(score[idx])