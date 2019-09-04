
result = []
for i in range(1,101):
    if i % 2 == 1:
#         result.append(str(i))
#
# print(result)
# print(', '.join(result))
# print(', '.join(map(str, result)))
        if i != 99:
            print(i, end=', ')
        else:
            print(i)

