'''
    선택정렬(Selection sort)
        1. 주어진 데이터 중, 최소값을 찾음
        2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
        3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

def selectionsort(data):
    for i in range(len(data)-1):
        selection = data[i]

        for j in range(len(data)-1-i): 
            if selection > data[j+i+1]:
                selection = data[j+i+1]
                data[i], data[j+i+1] = data[j+i+1], data[i]
    return data


import random
data_list = random.sample(range(100), 50)

print(data_list)
print("-----------------------------")
print(selectionsort(data_list))
 
sort = [5,4,3,2,1]
print(sort , "\n")
print(selectionsort(sort))

for i in range(3): # 0 1 2
    print(i)


'''
def selectionsort(data):
    for i in range(len(data)-1):
        selection = data[i] 
        selection_idx = i
        for j in range(len(data)-1-i): 
            if selection > data[j+i+1]:
                selection = data[j+i+1]
                selection_idx = j+i+1

        data[selection_idx] = data[i]
        data[i] = selection
    return data

sort = [5,4,3,2,1]
print(sort , "\n")
print(selectionsort(sort))
 
 # 선생님 코드
def selection_sort(data):
    for stand in range(len(data)-1):
        lowest = stand
        for index in range(stand+1, len(data)): 
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]    
    return data

import random

data_list = random.sample(range(100), 10)

print(data_list)
print("-----------------------------")
print(selection_sort(data_list))
