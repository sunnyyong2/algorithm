# fibonacci = []
# for i in range(10):
#     if i <= 1:
#         fibonacci.append(1)
#     else:
#         fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
# print(fibonacci)




fibonacci = []
for i in range(10):
    fibonacci.append(1) if i <= 1 else fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if i <= 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
print(fibonacci)



#조건표현식
# a = 2
# if a == 1:
#     print(True)
# else:
#     print(False)

# print(True) if a == 1 else print(False)