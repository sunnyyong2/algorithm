import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int, input().split()))
    ai = list(map(int, input().split()))

    # for i in ai:

        # print(max(ai[M]))
        # small_PLUS = ai[0:M]
        # small_PLUS.sort()
        # print(small_PLUS)
        # big_PLUS = ai[-M:]
        # print(abs(sum(big_PLUS) - sum(small_PLUS)))

    lst = []
    for i in range(N-M+1):
        lst.append(sum(ai[i:i+M]))
    print(max(lst) - min(lst))
    # print('#%s %d' % (tc, max(lst) - min(lst)))