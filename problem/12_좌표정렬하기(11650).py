'''
    제목 : 좌표 정렬하기
    난이도 : 하
    유형 : 정렬
    시간 : 15분
'''

'''
    문제풀이 핵심 아이디어
     1. (x좌표, y좌표)를 입력 받은 뒤 x좌표, y좌표 순서대로 차례대로 오름차순 정렬합니다.
     2. 파이썬의 기본 정렬 라이브러리는 기본적으로 튜플의 인덱스 순서대로 오름차순 정렬합니다.
     3. 따라서 단순히 기본 정렬 라이브러리를 이용하면 됩니다. (key 속성 설정 없이)
'''

num = int(input())
array = []

for _ in range(num):
    x, y = map(int, input().split(' '))
    array.append((x,y))

array = sorted(array)

for i in array:
    print(i[0], i[1])


# 두번째 시도 - 정답 - 정답과 거의 유사하다
array = list()
n = int(input())

for _ in range(n):
    x, y = map(int, input().split(' '))
    array.append((x,y))

array.sort()
for i in array:
    print(i[0] , i[1])
