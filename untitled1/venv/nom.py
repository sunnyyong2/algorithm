T = int(input())
for i in range(1,T+1):
    a,b = (input().split())
    if (a > b) :
        print('>')
    elif (a == b) :
        print('=')
    else:
        print('<')