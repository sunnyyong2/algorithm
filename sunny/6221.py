man1 = input()
man2 = input()
if man1 == '바위' and  man2 == '가위':
    print('Result : Man1 Win!')
elif man1 == '가위' and  man2 == '보':
    print('Result : Man1 Win!')
elif man1 == '보' and  man2 == '주먹':
    print('Result : Man1 Win!')
elif man1 == '바위' and  man2 == '바위':
    print('Result : Draw')
elif man1 == '가위' and  man2 == '가위':
    print('Result : Draw')
elif man1 == '보' and  man2 == '보':
    print('Result : Draw')