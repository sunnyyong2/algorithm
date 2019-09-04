for i in range(200):
    count = 0
    if i % 7 == 0 and i % 5 != 0:
        count += i
        print(count, end = ',')