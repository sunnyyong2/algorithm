import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ai = map(int, input())
    card = [0] * 10
    print(ai)
    # for i in ai:
    #     card[i] += 1
    # if max(card) == 1:
    #
    #     print(card.index(max(card)))

    # print(f'#{tc} {card.index(max(card))} {max(card)}')
