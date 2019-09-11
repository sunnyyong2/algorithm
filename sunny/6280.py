N = int(input())
LIST = []
for i in range(1,N+1):
    if N % i == 0:
        LIST.append(i)
print(LIST)



