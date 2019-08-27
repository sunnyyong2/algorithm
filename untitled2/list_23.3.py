# a = []
#
# for i in range(10):
#     a.append(1)
# print(a)
#
# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
# print(a)
#
# a = [[0 for j in range(2)] for i in range(3)]
# print(a)
#
# a = [[0]*2 for i in range(3)]
# print(a)
#
# a = [3,1,3,2,5]
# b = []
#
# for i in a:
#     line = []
#     for j in range(i):
#         line.append(0)
#     b.append(line)
#
# print(b)

# a = [[0]*i for i  in [3,1,3,2,5]]
# print(a)

students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
print(students)
print(sorted(students, key=lambda student: student[1]))
print(sorted(students, key=lambda student: student[2]))
print(sorted(students, key=lambda student: student[0][0]))
