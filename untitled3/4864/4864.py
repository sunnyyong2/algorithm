import sys
sys.stdin = open('input.txt', 'r')

#sol1)
T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print('1')
    else:
        print('0')

#sol2)
# T = int(input())
# for tc in range(1,T+1):
#     str1 = input().split()
#     str2 = input().split()
#     if str1[0] in str2[0]:
#         print('1')
#     else:
#         print('0')