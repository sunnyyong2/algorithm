import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ai = list(map(int, input()))
    card = [0] * 10
    for i in ai:
        card[i] += 1

    #내 코드 노우노우
    # if max(card) == 1:
    #     print(max(ai), max(card))

    #sol 1)
    # card = card[::-1]
    # print(9 - card.index(max(card)), max(card))

    #sol2)
    max_card = 0
    max_num = 0
    for i in range(len(card)):
        if card[i] >= max_card:
            max_card = card[i]
            max_num = i
    print(max_num, max_card)
