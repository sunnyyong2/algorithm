T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    for i in ai:
        print(max(ai[M]))







    # small_PLUS = ai[0:M]
    #
    # big_PLUS = ai[-M:]
    # print(abs(sum(big_PLUS) - sum(small_PLUS)))