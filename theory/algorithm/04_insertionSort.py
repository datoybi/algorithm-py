'''
    선택 정렬 (isnertion sort)

    반복문이 두개이기 때문에 O(n제곱)
    최악의 경우, n*(n-1)/2
    완전 정렬이 되어 있는 경우 O(n)

'''

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
