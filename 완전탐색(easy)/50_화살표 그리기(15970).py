'''
문제를 이해 못하겠따 씨빨!!!!
아니 왜 반대로 가능 방향의 c-a는 안하는지 모르겠다...
문제 이해함.. 
아.. 색깔 여러개... ㅅㅂ

5
0 1
1 2
3 1
4 2
5 1

13

7
6 1
7 2
9 1
10 2
0 1
3 1
4 1

16
'''
# 계산
def calculate(lst):
    lst.sort()
    sum = 0
    for i in range(len(lst)):
        if i == 0: # 0번째면
            sum += lst[1]-lst[0]  
        elif i == len(lst)-1: # 마지막 번째면
            sum += lst[i]-lst[i-1]
        else: # 중간꺼면
            sum += min(lst[i]-lst[i-1], lst[i+1]-lst[i])
    return sum

import sys

# 입력
total_lst = list()

for i in range(int(sys.stdin.readline())):
    item = list(map(int, sys.stdin.readline().split()))
    total_lst.append(item)

color_cnt, answer = total_lst[-1][0], 0

# 같은 색끼리 추출
for i in range(color_cnt):
    tmp_lst = list()
    for j in range(len(total_lst)):
        if total_lst[j][1] == i :
            tmp_lst.append(total_lst[j][0])
    answer += calculate(tmp_lst)

print(answer)

