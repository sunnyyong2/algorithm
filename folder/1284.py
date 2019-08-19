T = int(input())

for i in range(1,T+1):
    P,Q,R,S,W = list(map(int,input().split()))
    com_B = 0
    com_A = P * W
    com_B_1 = Q + ((W - R) * S)
    com_B_2 = R * Q

    if W > R:
        com_B = com_B_1
    else:
        com_B = com_B_2

    if com_B > com_A:
        print(com_A)
    else:
        print(com_B)
