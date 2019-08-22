
(i-1,j-1)      (i-1,j)      (i-1,j+1)
(i,j-1)        (i,j)        (i,j+1)
(i+1,j-1)      (i+1,j)      (i+1,j+1)

di = [0,1,1,1,0,-1,-1,-1]
dj = [1,1,0,-1,-1,-1,0,1]

cnt = 0
for i: 1 -> N-2
    for j: 1 -> N-2
        for k : 0 -> 7
            ni = i + di[k]
            nj = j + dj[k]
        if A[i][j]>max(a)
            cnt += 1


#확인
for i in range(8):
    print('.')
print(i)
