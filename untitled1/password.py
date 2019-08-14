p,k = list(map(int,input().split()))
count = 0
for assume_password in range(k,p+1):
    count += 1
print(count)