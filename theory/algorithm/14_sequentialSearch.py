'''
순차 탐색(Sequential Search)
    탐색은 여러 데이터 중에서 원하는 데이터를 찾아내는 것을 의미 
    데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법

    시간복잡도
        n번 비교 : O(n)

'''
# 내가 짠거
'''
def sequential_search(list, search):
    for i in range(len(list)):
        if list[i] == search:
            return i
    return False

import random
data_list = random.sample(range(10),10)

print(data_list)
print(sequential_search(data_list, 1))
'''

from random import *

rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1,10))

print(rand_data_list)


def sequential_search(data_list, search_data):
    for index in range(len(data_list)):
        if data_list[index] == search_data:
            return index
    return -1

print(sequential_search(rand_data_list,1))