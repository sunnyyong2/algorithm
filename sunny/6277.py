import sys
sys.stdin = open('temp.txt', 'r')

# numbers = [i for i in [int(input()) for _ in range(5)] if i % 2 == 0]
N = [int(input()) for _ in range(5)]
average = (N[0]+N[1]+N[2]+N[3]+N[4])/5
# numbers = []
# for _ in range(5):
#     num = int(input())
#
#         numbers.append(num)


print('입력된 값 {}의 평균은 {}입니다.' .format(N, average))
