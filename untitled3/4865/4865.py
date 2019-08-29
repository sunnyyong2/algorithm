import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    str1 = list(set(input()))
    str2 = list(input())

    # 값 초기화
    largest_value = 0  # 가장 큰 값을 저장하자!
    largest_alphabet = '' # 가장 큰 값의 알파벳을 저장하자!

    # str1을 돌면서 알파벳을 꺼내오자
    for char in str1:
        #str2에 들어있는 char를 세서 변수에 저장하자
        count_alphabet = str2.count(char)

        #만약 센 개수가 현재까지의 가장 큰 수보다 크면
        if count_alphabet > largest_value:

            #지금 센 개수를 최대 개수로 바꾼다
            largest_value = count_alphabet
            largest_alphabet = count_alphabet
    #제일 큰 수 출력하기
    print(largest_value)

























    #
    # max_value = 0
    # max_alpha = ''
    #
    # for char in str1:
    #     # print("{} : {}개".format(char, str2.count(char)))
    #
    #     count_alpha = str2.count(char)
    #
    #     if count_alpha > max_value:
    #         max_value = count_alpha
    #         max_alpha = char
    #
    # print(max_value)
