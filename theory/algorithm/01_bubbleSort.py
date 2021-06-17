'''

정렬(sorting)
    어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
    저열ㄹ은 프로그램 작성시 빈번하게 필요로 함 
    다양한 알고리즘이 고안되었으며, 알고리즘 학습의 필수
        다양한 정렬 알고리즘의 이해를 통해, 동일한 문제에 대해 다양한 알고리즘이 고안될 수 있음을 이해하고, 각 알고리즘간 선은비교를 통해, 알고리즘 성능 분석에 대해서도 이해할 수 있음

버블 정렬 (bubble sort)
    느리지만 단순
    두개씩 비교해가면서 큰 값을 뒤로 미는 정렬 

    시간복잡도 
        반복문이 두개이기 때문에 O(n제곱)
        최악의 경우 n*(n-1)/2
        완전 정렬이 되어 있는 상태라면 최선은 O(n)

'''
def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data)-index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break
    return data


import random

data_list = random.sample(range(100), 50)

print(data_list)
print("-----------------------------")
print(bubblesort(data_list))
