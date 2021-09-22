"""
    제목 : 수찾기
    난이도 : 하
    유형 : 해시, 배열, 구현
    시간 : 20분
"""
# n값 만큼 받는건 어떻게 받을까
# 시간 초과 뜸... 왠지는 모르겠다
# n = int(input())
# a = list(map(int, input().split(' ')))
# m = int(input())
# b = list(map(int, input().split(' ')))

# for i in b:
#     flag = 0
#     for j in a:
#         if i == j:
#             print('1')
#             flag = 1
#             break
#     if flag != 1:
#         print('0')

n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')


"""
    문제 풀이 핵심 아이디어
    1. 특정 정수의 등장 여부만을 간단히 체크하면 됩니다.
    2. Pyyhon에서는 dictionary 자료형을 해시처럼 사용할 수 있습니다.
    3. 본 문제는 set 자료형을 이용해 더욱 간단히 풀 수 있습니다. (집합 -> 중복x)
"""
