# T = int(input())
# for i in range(1,T+1):
#     Year, Month, Day = list(map(int,input().split()))
#     print(Year, Month, Day)
# if Month > 13 :
#     print(-1)
#     if Day > 30:
#         print('-1')
#     if Month == 2 and Day > 28:
#         print('-1')


T = int(input())
for i in range(1, T + 1):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    # ********************
    # result = '
    # for i in year:
    #     result += str(i)
    # print(result)
    # *********************
    #     Y = ''.join(map(str,year))
    #     M = ''.join(map(str,month))
    #     D = ''.join(map(str,day))
    if int(month) == 2 and int(day) > 28:
        print('-1')
    elif int(day) < 31 and 0 < int(month) < 13:
        print("{}/{}/{}".format(year, month, day))
    else:
        print('-1')





    # elif int(month) == 4 and int(day) > 30:
    #     print('-1')



