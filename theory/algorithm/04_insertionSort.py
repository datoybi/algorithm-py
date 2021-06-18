'''
    선택 정렬 (isnertion sort)
        하나씩 선택하여 비교

    반복문이 두개이기 때문에 O(n제곱)
    최악의 경우, n*(n-1)/2
    완전 정렬이 되어 있는 경우 O(n)


def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index + 1, 0, -1): # index+1부터 1까지 1만큼 감소
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break
    return data

import random
data_list = random.sample(range(100), 50)
print(insertion_sort(data_list))
 
'''
# 내가 생각하고 만든 selection 함수 - 이게 더 합당한 것 같다
def insertion_sort(data): 
    for index in range(len(data)-1):
        min = index
        for index2 in range(index+1, len(data)):
            if data[min] > data[index2]:
                min = index2
        data[min], data[index] = data[index], data[min]
    return data


import random
data_list = random.sample(range(100), 50)
print(insertion_sort(data_list))



