# 재귀용법을 활용한 프로그래밍 연습

# 다음 함수를 재귀 함수를 활용해서 완성해서 1부터 num까지의 곱이 출력되게 만드세요
'''
def multifly(n):
    if n <= 1:
        return n
    else:
        multifly(n-1)
        return n*(n-1)

print(multifly(4))


def multifly(num): # 반복문 사용
    return_value = 1
    for index in range(1, num+1):
        return_value = return_value * index
    return  return_value
        
def multifly(num): # 재귀함수 사용
    if num <= 1:
        return num
    return num * multifly(num-1)


# print(multifly(4))

#숫자가 들어있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요

def sum_list(data): # 반복문 사용
    total = 0
    for index in range(len(data)):
        total += data[index]
    return total

def sum_list2(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])
    

import random

data_list = random.sample(range(100),10)
print(data_list)
print(sum_list(data_list))
print(sum_list2(data_list))

'''

# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함 
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요

