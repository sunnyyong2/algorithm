score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0

#sol 1)
# for i in score:
#     if i >= 80:
#         total += i
# print(total)

#sol 2)
N = len(score) # 10
i = 0
while i < len(score): # N
    if score[i] >= 80:
        total += score.pop(i)
        i -= 1
    i += 1
print(total)

# print(score.pop(-2))
# print(score)

# sol 3)
# i = 0
# while i < len(score):
#     if score[i] >= 80:
#         total += score[i]
#     i += 1
# print(total)
