
# result = []
# for i in times_table:
#     for j in i:
#         if j % 3 != 0 and j % 7 != 0:
#             result.append(j)
# print(result)

result = []
for i in range(2,10):
    temp = []
    for j in range(1,10):
        # print('{} * {} = {}'.format(i, j, i * j))
        if (i * j) % 3 != 0 and (i * j) % 7 != 0:
            temp.append(i * j)
    result.append(temp)
print(result)


# temp = [1, 2, 3]
# # temp.extend([4, 5])
# temp += [4, 5]
# # temp.append([4, 5])
# print(temp)
#



