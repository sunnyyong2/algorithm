a = [[10,20], [30,40]]
# b = a
# b[0][0] = 500

b = a.copy()
b[0][0] = 500


print(a)
print(b)