T = int(input())

for tc in range(1,T+1):

    total = 0
    N = int(input())
    for i in range(1, N + 1):
        if i % 2 != 0:
            total += i
        else:
            total -= i
    print(f'#{tc} {total}')