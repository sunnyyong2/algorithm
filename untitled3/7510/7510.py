합이 N이 되는 연속된 자연수의 후보
1+2+...
2+3+...
3+4+...
4+5+...
N
cnt = 0
for i : 1 N -> #연속된 자연수의 시작 i,
        s = 0
        for j : i -> N #연속된 자연수 j
                    s += j
                    if s == N:
                        cnt += 1
                        break
                    elif s>N:
                        break
print(cnt)