'''
맞았습니다!

first in first out 
테스트 케이스 
문서의 개수 N (1~100), 현재 Queue에서 벛번째 놓여 있는지 나타내는 정수 M (0~N)
N개의 문서의 중요도가 차례로 주어짐

'''

import sys

for _ in range(int(sys.stdin.readline())):
    # 입력
    N, M = list(map(int, sys.stdin.readline().split()))
    queue = list(map(int, sys.stdin.readline().split()))
    lst = list()
    for i in range(len(queue)):
        lst.append([queue[i], chr(65+i)])
    word = lst[M][1]

    # 계산
    count = result = 0
    while True:
        max_value = 0
        for j in range(len(lst)):
            max_value = max(max_value, lst[j][0])
        if max_value == lst[0][0]:
            count += 1
            if lst[0][1] == word:
                result = count
            del lst[0]
        else:
            lst.append(lst[0])
            del lst[0]

        if len(lst) == 0:
            break
        
    print(result)
    





    