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

# 완벽히 일치하게 두번째 시도에서 품 

#세번째 시도 - 내장함수 안써서

n = int(input())
n_list = []
min_list = []

for _ in range(n):
    n_list.append(int(input()))

for i in range(len(n_list)):
    min = i
    for j in range(i+1, len(n_list)):
        if n_list[min] > n_list[j]:
            min = j;
    n_list[min], n_list[i] = n_list[i], n_list[min]

for item in n_list:
    print(item)
