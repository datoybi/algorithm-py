'''
    제목 : 수 정렬하기2
    난이도 : 하
    유형 : 정렬
    시간 : 20분 
    고급정렬 - 퀵, 병합, 힙
'''

# PyPy3로 메모리초과, Python3으로는 시간 초과
# test_case = int(input())
# data = []

# for i in range(test_case):
#     data.append(int(input()))

# def qsort(data):
#     if len(data) <= 1:
#         return data
#     pivot = data[0]

#     left = [item for item in data[1:] if pivot > item]
#     right = [item for item in data[1:] if pivot <= item]
#     return qsort(left) + [pivot] +qsort(right)

# qdata = qsort(data)

# for i in qdata:
#     print(i)

#맞았습니다! 떴음 , 해답  실제 시험에서는 이렇게
# test_case = int(input())
# data = []

# for _ in range(test_case):
#     data.append(int(input()))

# sotred_data = sorted(data)

# for i in sotred_data:
#     print(i)

'''
    문제풀이 핵심 아이디어
    - 데이터의 개수가 최대 1,000,000 개입니다.
    - 시간 복잡도 O(NlogN)의 정렬 알고리즘을 이용해야 합니다.
    - 고급 정렬 알고리즘 (병합정렬, 퀵정렬, 힙정렬 등)을 이용하여 문제를 해결 할 수 있습니다.
    - 혹은 파이썬의 기본 정렬 라이브러리를 이용하여 문제를 풀 수 있습니다.
    - 메모리가 허용된다면, 되도록 Python3보다는 PyPy3를 선택하여 코드를 제출합니다.

    병합정렬(Merge Sort) 알고리즘 
        - 분할 정복 방식을 이용 (devide and conquer)
        - 절반씩 합치면서 정렬하면, 전체 리스트가 정렬됩니다.
        - 시간 복잡도 O(NlogN)을 보장합니다.
    
'''

#해답
# 병합정렬 코드 
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)