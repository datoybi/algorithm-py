'''
퀵 정렬 (Quick sort) (분할 정복)
    정렬 알고리즘의 꽃 , 파이썬에서는 정말 아름다운 코드가 나온다
    기준점(pivot)을 정해서, 기준점보다 작은 데이터는 왼쪽(left), 큰 데이터는 오른쪽(right)으로 모으는 함수를 작성함
    각 왼쪽(left), 오른쪽(right)은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
    함수는 왼쪽(left) + 기준점(pivot) + 오른쪽(right)을 리턴함

    시간복잡도
        병합 정렬과 유사, 시간복잡도는 O(n log n)
        단 최악의 경우
            맨 처음 pivot이 가장 크거나, 가장 작으면
            모든 데이터를 비교하는 상황이 나옴 - O(n제곱)

'''

def qsort(data):
    if len(data) <=1 :
        return data
    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
        
    return qsort(left) + [pivot] + qsort(right)


import random

data_list = random.sample(range(100), 10)
print(qsort(data_list))

def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [data for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]
    return qsort(left) + [pivot] + qsort(right)