"""
    제목 : 수 정렬하기
    난이도 : 하
    유형 : 정렬
    시간 : 15분

"""

# 내코드

num = int(input())
arr = []

for _ in range(num):
    data = int(input())
    arr.append(data)

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        # print(i , " , " , j)
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i] 
            # min = arr[j]
    print(arr[i])


"""
    문제 풀이 핵심 아이디어 : 데이터의 개수가 1000개 이하이므로 기본적인 정렬 알고리즘으로 해결할 수 있습니다.
"""

# 1) 선택정렬 알고리즘으로 문제 해결하기

# n = int(input())
# array = list()

# for _ in range(n):
#     array.append(int(input()))

# for i in range(n):
#     min_index = 1
#     for j in range(i+1, n):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]

# for i in array:
#     print(i)


# 2. 파이썬의 기본 정렬 라이브러리로 문제 해결하기
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)