'''
맞았습니다!
의상 수 0~30

반례
1
6
hat headgear
sunglasses eyewear
turban headgear
lens eyewear
glasses eyewear
sunglasses face

답 23
'''

import sys

for _ in range(int(sys.stdin.readline())):
    accessories = list()

    for _ in range(int(sys.stdin.readline())):
        name, category = map(str, sys.stdin.readline().split())
        accessories.append([category, name])

    arr = list()
    for i in range(len(accessories)):
        tmp = list()
        for j in range(len(accessories)):
            if accessories[i][0] == accessories[j][0]:
                tmp.append(accessories[j][1])
        if tmp not in arr:
            arr.append(tmp)

    # print(arr) # [['hat', 'turban'], ['sunglasses']] 
    # arr의 각각의 리스트 길이+1를 다 곱한 뒤 -1을 하면 답나옴
    sum = 1
    for i in range(len(arr)):
        sum *= len(arr[i])+1 

    if len(accessories) == 0:
        print('0') 
    else:
        print(sum-1) 



# 남 코드 간결해서 가져와봄

# from collections import Counter
# t = int(input())
# for i in range(t):
#     n = int(input())
#     s = []
#     for j in range(n):
#         a, b = input().split()
#         s.append(b)
#     print(s)
    
#     num = 1
#     result = Counter(s)
#     for key in result:
#         num *= result[key] + 1
#     print(num - 1)