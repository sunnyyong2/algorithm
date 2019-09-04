i = 7 # * 찍을 변수
j = 0 # '빈칸' 을 찍을 변수
while True:
    print(' ' * j, end='')
    print('*' * i)
    if i==1:
        break
    i -= 2
    j += 1
