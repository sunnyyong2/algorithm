T = int(input())

for tc in range(1,T+1):
    text = input().split()
    # if text == text[::-1]:

    if text == (text[0][::-1]):
        print('1')
    else:
        print('0')