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

    참고
    [표현식 for 항목 in 리스트 if 조건문]
'''

def qsort(data):
    if len(data) <=1:
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

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]
    return qsort(left) + [pivot] + qsort(right)


import random

data_list = random.sample(range(100), 10)
#print(qsort([5,4,3,2,1]))
print(qsort(data_list))


'''
# 다음 리스트를 리스트 슬라이싱(예 [:2])을 이용해서 세 개로 짤라서 각 리스트 변수에 넣고 출력해보기

data_list = [1,2,3,4,5]

data1 = data_list[:2]
data2 = data_list[3]
data3 = data_list[3:]

print(data1)
print(data2)
print(data3)

# 다음 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣기

data_list = [1,2,3,4,5]
left = list()
right = list()

for index in range(1, len(data_list)):
    if data_list[0] > data_list[index]:
        left.append(data_list[index])
    else:
        right.append(data_list[index])
    
print("left: " , left)
print("right: " , right)

# 다음 리스트를 맨 앞에 데이터를 pivot 변수에 넣고, pivot 변수 값을 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣기
# data_list 가 임의 길이일 때 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣기

import random

data_list = random.sample(range(100),10)
left = list()
right = list()
pivot = data_list[0]

for index in range(1, len(data_list)):
    if pivot > data_list[index]:
        left.append(data_list[index])
    else:
        right.append(data_list[index])

print(left , right)

# data_list 가 다음 세 데이터를 가지고 있을 때 리스트를 맨 앞에 데이터를 기준으로 작은 데이터는 left 변수에, 그렇지 않은 데이터는 right 변수에 넣고 left, right, pivot 변수 값을 사용해서 정렬된 데이터 출력해보기
# 잘못됨

data_list = [4,3,2]
pivot = data_list[0]
arranged_data = list()
left, right = list(), list()


for index in range(1, len(data_list)):
    if pivot > data_list[index]:
        left = data_list[index]
    else:
        right = data_list[index]

arranged_data = left + [pivot] + right

#print(left, right)
print(arranged_data)    

'''
