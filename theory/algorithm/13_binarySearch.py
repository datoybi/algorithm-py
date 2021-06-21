'''
    분할정복 알고리즘과 이진탐색
    분할정복 알고리즘 (Divide and Conquer)
        Divide: 문제를 하나 또는 둘 이상으로 나눈다.
        Conquer: 나눠진 문제가 충분히 작고, 해결이 가능하다면 해결하고, 그렇지 않다면 다시 나눈다.
    
    이진탐색
        Divide: 오름차순으로 정렬된 리스트를 두개의 서브 리스트로 나눈다.
        Conquer
            검색할 숫자(search) > 중간값이면 뒷 부분의 서브 리스트에서 검색할 숫자를 찾는다.
            검색할 숫자(search) < 중간값이면 앞 부분의 서브 리스트에서 검색할 숫자를 찾는다.

참고 
    list[1:] : 첫번째 제외하고 그 다음부터 슬라이싱
    list[:1] : 첫번째까지 슬라이싱
'''

def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False
    medium = len(data) // 2 # 몫 구함
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)

import random

data_list = random.sample(range(), 10)
data_list.sort()
print(data_list)
print(binary_search(data_list, 7))


'''
    시간복잡도
        n에 1/2를 1이 될 때 까지 곱한다.
        O(logn)
        
'''