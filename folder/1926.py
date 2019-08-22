N = int(input())

for i in range(1, N + 1):

    # 스트링으로 바꾼 숫자에
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
    # sol 1
        count = 0

        for char in str(i):
            if char == '3' or char == '6' or char == '9':
                count += 1

        print(count * "-", end=' ')
    # sol 2 -> 안추천
    #     if str(i).count('3'):
    #         print('-', end=' ')
    #     if str(i).count('6'):
    #         print('-', end=' ')
    #
    #     if str(i).count('9'):
    #         print('-', end=' ')
    else:
        print(str(i), end=' ')
