'''
    병합정렬 (merge sort)
        분할 정복 알고리즘을 사용하는 정렬 기법 
        1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
        2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
        3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
        
        초큼 어렵다 구현이 담에 또 봐보자

'''

def split(data):
    medium = int(len(data)/2)
    left = data[:medium]
    right = data[medium:]
    print(left, right)

data_list = [3,4,1,3,2]
split(data_list)

def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data)/2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    #case1: left/right 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1
    #case2: left만 남아 있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    #case3: right만 남아 있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


import random

data_list = random.sample(range(100), 10)
print(mergesplit(data_list))
