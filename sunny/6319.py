palindrome = input()
if palindrome[0] == palindrome[0][::-1]:
    print(palindrome)
    print(f'입력하신 단어는 회문(Palindrome)입니다.')