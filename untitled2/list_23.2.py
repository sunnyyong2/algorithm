a = [[10,20],[30,40],[50,60]]

# for i in range(len(a)):
#     print(len(a[i]))
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')

# i = 0
# while i < len(a):
#     x,y = a[i]
#     i += 1
#     print(x,y)

i = 0
while i < len(a):
     j = 0
     while j < len(a[i]):
         print(a[i][j], end = ' ')
         j += 1
     print()
     i += 1