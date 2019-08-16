T = int(input())
for tc in range(1,T+1):
    text = input()
    for i in range(tc):
        if tc == tc.reverse():
            print('1')
        else:
            print('0')