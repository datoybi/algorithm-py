'''
    제목 : 수 정렬하기 3
    난이도 : 하 
    유형 : 정렬
    시간 : 20분

'''

# 왜 메모리 초과가 뜨는 지 알 수 없다.
# num = int(input())
# data = []
# arrange_data = []

# for i in range(num):
#     data.append(int(input()))

# arrange_data = sorted(data)

# for j in arrange_data:
#     print(j)

"""
    계수 정렬(Counting Sort) 알고리즘
        - 배열의 인덱스를 특정한 데이터의 값을 여기는 정렬 방법입니다.
        - 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정합니다.
        - 데이터가 등장한 횟수를 셉니다.

    유의사항 : 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()을 사용해야 합니다.
"""

# 이 자체가 계수정렬

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n): # 입력
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001): # 출력 
    if array[i] != 0:
        for _ in range(array[i]):
            print(i)


# 두번째 시도에서도 메모리 초과가 난다. - 답지 보고 이해한 뒤 함 - 
# 근데 while문을 썼는데 메모리 초과가 뜸.. 왜인지는 모르겠다.
import sys

n = int(sys.stdin.readline())
array = [0] * 10001

# print(array)

# 입력
for i in range(n): 
    data = int(sys.stdin.readline())
    array[data] += 1

# print(array)

# 출력
for i in range(10001):
    while array[i] != 0:
        print(i)
        array[i] -= 1

