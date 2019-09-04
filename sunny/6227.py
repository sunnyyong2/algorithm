for i in range(100,300):
    count = 0
    if (str(i)[0]) == 2:
        if (str(i)[1]) % 2 == 0:
            if (str(i)[2]) % 2 == 0:
                count += i
                print(str(i))
