maxV = 0
#행의 합
for i : 0 -> 99
        s = 0 #행의 합. 행이 바뀔 때 초기화
        for j : 0 -> 99
            s = s + arr[i][j]
        if maxV <s  #행의 합과 비교
            maxV = s
#열의 합
for i : 0 -> 99 # 열 고정
        s = 0 #열의 합. 열이 바뀔 때 초기화
        for j : 0 -> 99 #행
            s = s + arr[j][i]
        if maxV <s #열의 합과 비교
            maxV = s

#두 대각선의 합
s = 0 #오른쪽 아래 방향
for i : 0 -> 99
        s = s + arr[i][i]
if maxV < s
        maxV = s
s = 0 #왼쪽 아래 방향(0,99), (1,98), (2,97) ... (99,0)
for i : 0 -> 99
        s = s + arr[i][99-i] #N X N인 경우 arr[i[N-1-i]


        s1 = 0 #행의 합
        s2 = 0 #열의 합
        for j: 0 -> 99
            s1 = s + arr[i][j]
            s2 = s + arr[j][i]
        if maxV < s1  # 행의 합과 비교
            maxV = s1
        if maxV < s2  # 행의 합과 비교
            maxV = s2

        s3 = 0 #오른쪽 아래
        s4 = 0 #왼쪽 아래
        for i: 0 -> 99
            s1 = 0
            s2 = 0
            s3 = s3 + arr[i][j]
            s4 = s4 + arr[i][99-i]
            for j : 0 -> 99
            s1 = s + arr[i][j]
            s2 = s + arr[j][i]
            if maxV < s1  # 행의 합과 비교
                maxV = s1
            if maxV < s2  # 행의 합과 비교
                maxV = s2
            if maxV <s3
                maxV = s3
            if maxV <s4
                maxV = s4
