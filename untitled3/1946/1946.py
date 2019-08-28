import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    #word를 만들어서  word에 값 추가!
    word = ''

    for i in range(N):
        C, K = input().split()

        word += C * int(K)

    #알파벳 합쳐서 10개씩 잘라!
    # 방법 1
    for j in range(0, len(word), 10):
        print(f'#{tc} {word[j:j + 10])

    # 방법 2
    start = 0
    end = 10
    while start < len(word):
        print(word[start:end])
        start += 10
        end += 10
