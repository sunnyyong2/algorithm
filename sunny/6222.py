text = input()
ascii = ord('c')
print(ascii)
if 'a' <= text <= 'z':
    ascii2 = ascii - 32
    print('c(ASCII: ascii) => C(ASCII: ascii2)')
elif 'A' <= text <= 'Z':
    ascii2 = ascii + 32
    print('c(ASCII: ascii2) => C(ASCII: ascii)')
# else:
#     print(text)