s = input()   #Algorithm algo   #세 가지 방식들의 차이점
print(s)
s = input().split() #s : 'algorithm'
print(s)
s = list(input())  #'ABCD' => 'A', 'B', 'C', 'D'
#'A' <-> 'D', 'B' <-> 'C' 총 교환 횟수는 글자수 //2
for i in range(0,len(s)//2): #4/2 -> 2회, 인덱스 0,1
    s[i], s[len(s)-1-i], s[i]
print(s)
for i in range(0,len(s)):
    print(s[i],end='')
print()
open = s[::-1]
print(''.join(s))
