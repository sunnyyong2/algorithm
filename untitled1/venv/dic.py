alphabets = input()

# 참고할 사전을 만들었다고 한다
mate = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

for alphabet in alphabets:
    test = mate.get(alphabet)
    test2 = meta[alphabet]
    print(test)

# print(mate[alphabets])

# 딕셔너리를 좀 더 편하게 만드는 법
# dict_1= {}
# alphabets2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# count = 0
# for char in alphabets2:
#     count += 1
#     dict_1[char] = count
# print(dict_1)